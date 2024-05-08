from django.contrib import admin
from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'product', 'document', 'start_date', 'end_date', 'cost'
