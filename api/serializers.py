from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Product
        fields = (
            'id',
            'name',  # Name of the product
            'img',  # Image of the product
            'description',  # Description of the product
            'course_number',  # Course number, optional
            'professor',  # Name of the professor, optional
            'category',  # Category of the product
            'price',  # Price of the product
            'user',
            'email',
            'created_at',  # Timestamp when the product was created
            'sold',  # Boolean indicating if the product is sold
        )

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'products')
    
