from django.urls import path

from ads.views import (
    AdsListView,
    AdsCreateView,
    AdsDetailsView,
    AdsUpdateView,
    AdsDeleteView,
    AdsStatisticsListView
)

app_name = 'ads'

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
    path('new/', AdsCreateView.as_view(), name='ads_create'),
    path('<int:pk>/', AdsDetailsView.as_view(), name='ads_detail'),
    path('<int:pk>/edit/', AdsUpdateView.as_view(), name='ads_update'),
    path('<int:pk>/delete/', AdsDeleteView.as_view(), name='ads_delete'),
    path('statistic/', AdsStatisticsListView.as_view(), name='ads_static'),
    ]

