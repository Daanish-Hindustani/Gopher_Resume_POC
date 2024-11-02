from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.permissions import IsAuthenticated
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
