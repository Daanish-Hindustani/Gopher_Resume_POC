from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException

import logging
logger = logging.getLogger(__name__)

class NotFound(APIException):
    status_code = 404
    default_detail = 'Sorry!! Not Found'

class ProductList(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        logger.info("/products list API got called..")
        return super().list(request, *args, **kwargs)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    throttle_classes = [UserRateThrottle]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        logger.info("/product detail API got called..")
        try:
            return super().retrieve(request, *args, **kwargs)
        except ObjectDoesNotExist:
            logger.error("Product not found")
            raise NotFound()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
