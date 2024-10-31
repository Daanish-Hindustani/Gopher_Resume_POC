from django.urls import path
from .views import *

urlpatterns = [
    path('', market, name='market'),
    path('product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
