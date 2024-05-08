from django.contrib import admin
from leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = 'pk', 'first_name', 'last_name', 'phone', 'email', 'ads'