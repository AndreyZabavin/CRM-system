from django.db import models
from ads.models import Ads


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
