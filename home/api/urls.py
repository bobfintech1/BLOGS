from django.urls import path, include

from home.api.views import home_api_view, create_home_api, home_delete_api_view, home_detail_api_view, \
    comments_home_view, comment_create_view

app_name = 'home'

urlpatterns = [
    path('home_view/', home_api_view, name='home'),
    path('create', create_home_api, name='create'),
    path('create_comm', comment_create_view, name='comment_create'),
    path('comment/<int:pk>', comments_home_view, name='comment'),
    path('delete/<int:pk>', home_delete_api_view, name='delete'),
    path('detail/<int:pk>', home_detail_api_view, name='detail')
]