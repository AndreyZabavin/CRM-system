import os
from django.db import models
from products.models import Product


def upload_path(instance, filename):
    doc_name = instance.name
    extension = os.path.splitext(filename)[1]
    return f'contracts/document/{doc_name}{extension}'


class Contract(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    document = models.FileField(upload_to=upload_path)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

