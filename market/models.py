from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Enum choices for category
    CLOTHING = 'CLOTHING'
    BOOKS = 'BOOKS'
    OTHER = 'OTHER'
    CATEGORY_CHOICES = [
        (CLOTHING, 'Clothing'),
        (BOOKS, 'Books'),
        (OTHER, 'Other'),
    ]

    # Product fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/product', blank=True, null=True)
    description = models.TextField(blank=True)
    course_number = models.CharField(max_length=50, blank=True, null=True)
    professor = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHER)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    user_email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

