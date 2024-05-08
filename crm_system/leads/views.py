from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from leads.models import Lead


class LeadsListView(PermissionRequiredMixin, ListView):
    permission_required = 'leads.view_lead'
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        return Lead.objects.filter(customer__isnull=True)


class LeadCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'leads.add_lead'
    template_name = 'leads/leads-create.html'
    queryset = Lead.objects.select_related('ads')
    fields = 'first_name', 'last_name', 'phone', 'email', 'ads'
    success_url = reverse_lazy('leads:leads_list')


class LeadDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'leads.view_lead'
    template_name = 'leads/leads-detail.html'
    model = Lead


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'leads.change_lead'
    template_name = 'leads/leads-edit.html'
    queryset = Lead.objects.select_related('ads')
    fields = 'first_name', 'last_name', 'phone', 'email', 'ads'

    def get_success_url(self):
        return reverse('leads:lead_detail', kwargs={'pk': self.object.pk})


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'leads.delete_lead'
    template_name = 'leads/leads-delete.html'
    model = Lead
    success_url = reverse_lazy('leads:leads_list')

