import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from decouple import config, Csv


@csrf_exempt
def sign_in(request):
    return render(request, 'userauth/sign_in.html')


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside auth_receiver')
    token = request.POST.get('credential')  # Safely retrieve the token

    if not token:
        return HttpResponse("Missing credential in the POST data.", status=400)
    
    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), config('CLIENT_ID')
        )
    except ValueError:
        return HttpResponse("Invalid token", status=403)

    # Save user data to the session or database as needed
    request.session['user_data'] = user_data

    return redirect('sign_in')

def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')

