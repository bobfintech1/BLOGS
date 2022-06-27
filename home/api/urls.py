from django.urls import path, include

from home.api.views import home_api_view, create_home_api, home_delete_api_view, home_detail_api_view

app_name = 'home'

urlpatterns = [
    path('home_view/', home_api_view, name='home'),
    path('create', create_home_api, name='create'),
    path('delete/<int:pk>', home_delete_api_view, name='delete'),
    path('detail/<int:pk>', home_detail_api_view, name='detail')
]