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

    def get(self, request):
        print(request.user)  # Check if the user is authenticated
        product_id = request.GET.get('product_id')
        if product_id:
            product_data = load_item(product_id)
            return render(request, 'market/market.html', {'product_data': product_data})
        else:
            products_data = load_items()
            return render(request, 'market/market.html', {'product_data': products_data})



def load_item(product_id):
    try:
        url = f"http://{host}/api/products/{product_id}/"  # Replace with the actual endpoint
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve product:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error during the request:", e)
        return None


def load_items():
    try:
        url = f"http://{host}/api/products/"  # Replace with the actual endpoint for listing products
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve products:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error during the request:", e)
        return None
