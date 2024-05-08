from django.db import models
from products.models import Product


class Promotion(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
