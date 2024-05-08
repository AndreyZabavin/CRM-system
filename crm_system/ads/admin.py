from django.contrib import admin
from ads.models import Ads, Promotion


@admin.register(Ads)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'product', 'promotion', 'budget'


@admin.register(Promotion)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'