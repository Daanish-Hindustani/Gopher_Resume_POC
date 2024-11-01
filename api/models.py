
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Product(models.Model):

    # Enum choices for category
    CLOTHING = 'CLOTHING'
    BOOKS = 'BOOKS'
    FURNITURE = 'FURNITURE'
    ELECTRONICS = 'ELECTRONICS'
    SPORTS = 'SPORTS'
    SCHOOL_SUPPLIES = 'SCHOOL_SUPPLIES'
    OTHER = 'OTHER'

    CATEGORY_CHOICES = [
        (SCHOOL_SUPPLIES, 'School Supplies'),
        (SPORTS, 'Sports'),
        (ELECTRONICS, 'Electronics'),
        (FURNITURE, 'Furniture'),
        (CLOTHING, 'Clothing'),
        (BOOKS, 'Books'),
        (OTHER, 'Other'),
    ]

    # Product fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/product', default='img/product/dummy.png', blank=True, null=True)
    description = models.TextField(blank=True)
    course_number = models.CharField(max_length=50, blank=True, null=True)
    professor = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHER)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    def slug(self):
        return slugify(self.title)
    
    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    @property
    def in_stock(self):
        return self.sold
    
    def __str__(self):
        return self.name
