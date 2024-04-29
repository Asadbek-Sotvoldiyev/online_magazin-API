from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    about = models.TextField()
    price = models.DecimalField(max_digits=10000000, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    created_time = models.DateTimeField(auto_now_add=True)
