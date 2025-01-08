from django.shortcuts import render
from django.views import View
import requests
from decouple import config
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Load the host URL from environment variable
host = config('HOST')


class MarketView(View):

    def get(self, request, *args, **kwargs):
        print('token', request.session['user_data']['auth_token'])
        token = request.session['user_data']['auth_token']
        
        # Get the product_id from URL arguments
        product_id = kwargs.get('product_id')

        if product_id:
            product = load_item(product_id, token)  
            return render(request, 'market/product_detail.html', {
                'product': product,
            })
        else:
            product_data = load_items(token)  # Get all products
            return render(request, 'market/market.html', {'product_data': product_data})



def load_item(product_id, token):
    try:
        url = f"http://{host}/api/products/{product_id}/"
        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return {'is_list': False, **response.json()}  # Include 'is_list' for template logic
        else:
            print("Failed to retrieve product:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error during the request:", e)
        return None


def load_items(token):
    try:
        url = f"http://{host}/api/products/"
        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return {'is_list': True, 'product_data': response.json()}  
        else:
            print("Failed to retrieve products:", response.status_code, response.text)
            return {'is_list': True, 'product_data': []}
    except requests.exceptions.RequestException as e:
        print("Error during the request:", e)
        return {'is_list': True, 'data': []}
