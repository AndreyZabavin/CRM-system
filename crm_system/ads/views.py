from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Sum, F
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from ads.models import Ads


class AdsListView(PermissionRequiredMixin, ListView):
    permission_required = 'ads.view_ads'
    template_name = 'ads/ads-list.html'
    model = Ads
    context_object_name = 'ads'


class AdsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'ads.add_ads'
    template_name = 'ads/ads-create.html'
    queryset = Ads.objects.select_related('product', 'promotion')
    fields = 'name', 'product', 'promotion', 'budget'
    success_url = reverse_lazy('ads:ads_list')


class AdsDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = 'ads.view_ads'
    template_name = 'ads/ads-detail.html'
    queryset = Ads.objects.select_related('product')


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'ads.change_ads'
    template_name = 'ads/ads-edit.html'
    queryset = Ads.objects.select_related('product', 'promotion')
    fields = 'name', 'product', 'promotion', 'budget'

    def get_success_url(self):
        return reverse('ads:ads_detail', kwargs={'pk': self.object.pk})


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'ads.delete_ads'
    template_name = 'ads/ads-delete.html'
    model = Ads
    success_url = reverse_lazy('ads:ads_list')


class AdsStatisticsListView(ListView):
    model = Ads
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            leads_count=Count('lead'),
            customers_count=Count('lead__customer'),
            total_contract_cost=Sum('lead__customer__contract__cost'),
            profit=F('total_contract_cost') - F('budget')
        )
        return queryset
