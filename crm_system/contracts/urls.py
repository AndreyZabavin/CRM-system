from django.urls import path

from contracts.views import (
    ContractsListView,
    ContractCreateView,
    ContractDetailsView,
    ContractUpdateView,
    ContractDeleteView
)

app_name = 'contracts'

urlpatterns = [
    path('', ContractsListView.as_view(), name='contracts_list'),
    path('new/', ContractCreateView.as_view(), name='contract_create'),
    path('<int:pk>/', ContractDetailsView.as_view(), name='contract_detail'),
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_update'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete')
]

