from django.urls import path

from accounts.views import MyLogin, MyLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLogin.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
