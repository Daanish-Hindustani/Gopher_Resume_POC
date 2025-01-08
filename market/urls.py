from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketView.as_view(), name='market'),  
    path('product/<int:product_id>/', views.MarketView.as_view(), name='product'),  
]