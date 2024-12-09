from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketView.as_view(), name='market'),  # Set the path to use MarketView
    path('product/', views.MarketView.as_view(), name='market'),  # You can keep both paths if needed
]