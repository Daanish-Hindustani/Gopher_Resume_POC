from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# When the market endpoint is hit, the page will load with all items
def market(request):
    product_list = Product.objects.order_by("-created_at")
    context = {"product_list": product_list}
    return render(request, "market/index.html", context)

