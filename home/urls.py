from django.urls import path
from accounts.views import *
from home.views import *

app_name ='home'

urlpatterns = [
    path('home_list/', home_list, name='home_list'),
    path('create', home_create, name='create'),
    path('detail-home/<int:pk>', detail_home_view, name='detail'),
    path('detail/<int:pk>', detail_home_carousel, name='detail_carousel'),
    path('update/<int:pk>', edit_home_view, name='update_carousel'),


    # path('home_main/', home_main, name='home_main'),
]