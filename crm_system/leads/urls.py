from django.urls import path

from leads.views import (
    LeadsListView,
    LeadCreateView,
    LeadDetailsView,
    LeadUpdateView,
    LeadDeleteView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadsListView.as_view(), name='leads_list'),
    path('new/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/', LeadDetailsView.as_view(), name='lead_detail'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete')
]

