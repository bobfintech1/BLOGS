from django.urls import path
from accounts.api.views import registration_view, account_detail_view, update_account_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = "accounts"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('detail', account_detail_view, name="properties"),
    path('update', update_account_view, name="properties"),
    path('login', obtain_auth_token, name="login"),
]