from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from contracts.models import Contract


class ContractsListView(PermissionRequiredMixin, ListView):
    permission_required = 'contracts.view_contract'
    template_name = 'contracts/contracts-list.html'
    model = Contract
    context_object_name = 'contracts'


class ContractCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'contracts.add_contract'
    template_name = 'contracts/contracts-create.html'
    queryset = Contract.objects.select_related('product')
    fields = 'name', 'product', 'document', 'start_date', 'end_date', 'cost'
    success_url = reverse_lazy('contracts:contracts_list')


class ContractDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'contracts.view_contract'
    template_name = 'contracts/contracts-detail.html'
    queryset = Contract.objects.select_related('product')


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'contracts.change_contract'
    template_name = 'contracts/contracts-edit.html'
    queryset = Contract.objects.select_related('product')
    fields = 'name', 'product', 'document', 'start_date', 'end_date', 'cost'

    def get_success_url(self):
        return reverse('contracts:contract_detail', kwargs={'pk': self.object.pk})


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'contracts.delete_contract'
    template_name = 'contracts/contracts-delete.html'
    model = Contract
    success_url = reverse_lazy('contracts:contracts_list')

