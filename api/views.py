from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import api_view, throttle_classes
from django.views.decorators.cache import cache_page
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException

class NotFound(APIException):
    status_code = 404
    default_detail = 'Sorry!! Not Found'

import logging
logger = logging.getLogger(__name__)

class ProductList(generics.ListCreateAPIView):
    logger.info("/products list API got called..")
    renderer_classes = (JSONRenderer, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    logger.info("/product detail API got called..")
    renderer_classes = (JSONRenderer, )
    throttle_classes([UserRateThrottle])
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @cache_page(60 * 10)
# def ProductListPage(request):
#     logger.info("/product list page got called..")
#     try:
#         products = Product.objects.all()
#         for product in products:
#             product.img = str(product.img).split('/')[-1]
#     except ObjectDoesNotExist as e:
#         logger.error(e.message)
#         raise Http404
#     return render(request, 'journal/list.html', {'articles':products})

# @cache_page(60 * 30)
# def ProductDetailPage(request, pk):
#     logger.info("/product details page got called for pk", pk)
#     return render(request, 'journal/detail.html', {'product_id':pk} )