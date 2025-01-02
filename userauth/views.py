from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from decouple import config
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

def sign_in(request):
    """Render the sign-in page with Google OAuth button."""
    if request.user.is_authenticated:
        return redirect('market/')
    return render(request, 'userauth/sign_in.html')

@csrf_exempt  # Only for Google OAuth callback
def auth_receiver(request):
    """Handle Google OAuth callback and create/update user in database."""
    token = request.POST.get('credential')
    
    if not token:
        logger.error("Missing credential in POST data")
        return HttpResponse("Missing credential in the POST data.", status=400)
    
    try:
        # Verify the Google OAuth token
        user_data = id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            config('CLIENT_ID')
        )
        
        # Extract user information from Google data
        email = user_data['email']
        first_name = user_data.get('given_name', '')
        last_name = user_data.get('family_name', '')
        
        # Try to get existing user or create new one
        try:
            user = User.objects.get(email=email)
            # Update existing user's information
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            logger.info(f"Existing user logged in: {email}")
        except User.DoesNotExist:
            # Create new user
            username = email.split('@')[0]  # Use email prefix as username
            # Handle username conflicts
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            logger.info(f"New user created: {email}")
        
        # Create or get authentication token
        token, _ = Token.objects.get_or_create(user=user)
        
        # Log the user in
        login(request, user)
        
        # Store additional user data in session if needed
        request.session['user_data'] = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'picture': user_data.get('picture', ''),
            'auth_token': token.key
        }
        print('token',token)
        return redirect('market/')
        
    except ValueError as e:
        logger.error(f"Token verification failed: {str(e)}")
        return HttpResponse("Invalid token", status=403)
    except Exception as e:
        logger.error(f"Authentication error: {str(e)}")
        return HttpResponse("Authentication failed", status=500)

def sign_out(request):
    """Handle user sign out."""
    if 'user_data' in request.session:
        del request.session['user_data']
    logout(request)
    return redirect('sign_in')