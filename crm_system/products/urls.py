from django.urls import path

from products.views import (
    ProductListView,
    ProductCreateView,
    ProductDetailsView,
    ProductUpdateView,
    ProductDeleteView
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product_detail'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]

