from django.contrib import admin
from api.models import Product
from django.contrib.auth.models import User

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
            'id',  # Auto-incrementing primary key
            'name',  # Name of the product
            'img',  # Image of the product
            'description',  # Description of the product
            'course_number',  # Course number, optional
            'professor',  # Name of the professor, optional
            'category',  # Category of the product
            'user',  # Foreign key to the User model
            'price',  # Price of the product
            'created_at',  # Timestamp when the product was created
            'sold',  # Boolean indicating if the product is sold
        )


admin.site.register(Product, ProductAdmin)
