from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50)
    product_image=models.ImageField(upload_to="products/",blank=True,null=True)
    product_file = models.FileField(upload_to="products/files/",blank=True,null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
