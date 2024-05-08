from django.urls import path

from customers.views import (
    CustomersListView,
    CustomerCreateView,
    CustomerDetailsView,
    CustomerUpdateView,
    CustomerDeleteView
)

app_name = 'customers'

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers_list'),
    path('new/', CustomerCreateView.as_view(), name='customers_create'),
    path('<int:pk>/', CustomerDetailsView.as_view(), name='customers_detail'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customers_update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customers_delete')
]

