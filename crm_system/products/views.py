from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'products.view_product'
    template_name = 'products/products-list.html'
    model = Product
    context_object_name = 'products'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'products.add_product'
    template_name = 'products/products-create.html'
    model = Product
    fields = 'name', 'description', 'cost'
    success_url = reverse_lazy('products:products_list')


class ProductDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'products.view_product'
    template_name = 'products/products-detail.html'
    model = Product


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'products.change_product'
    template_name = 'products/products-edit.html'
    model = Product
    fields = 'name', 'description', 'cost'

    def get_success_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'products.delete_product'
    template_name = 'products/products-delete.html'
    model = Product
    success_url = reverse_lazy('products:products_list')

