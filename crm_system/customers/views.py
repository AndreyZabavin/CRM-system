from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from customers.models import Customer
from leads.models import Lead


class CustomersListView(PermissionRequiredMixin, ListView):
    permission_required = 'customers.view_customer'
    template_name = 'customers/customers-list.html'
    model = Customer
    context_object_name = 'customers'


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'customers.add_customer'
    template_name = 'customers/customers-create.html'
    model = Customer
    fields = 'lead', 'contract'
    success_url = reverse_lazy('customers:customers_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['lead'].queryset = Lead.objects.filter(customer__isnull=True)
        return form


class CustomerDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'customers.view_customer'
    template_name = 'customers/customers-detail.html'
    queryset = Customer.objects.select_related('lead')


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'customers.change_customer'
    template_name = 'customers/customers-edit.html'
    queryset = Customer.objects.select_related('lead', 'contract')
    fields = 'lead', 'contract'

    def get_success_url(self):
        return reverse('customers:customers_detail', kwargs={'pk': self.object.pk})


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'customers.delete_customer'
    template_name = 'customers/customers-delete.html'
    model = Customer
    success_url = reverse_lazy('customers:customers_list')

