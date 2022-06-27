"""Blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import registration_view, home_view, account_login, signout, edit_account_view
from home.views import home_list, delete_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_list, name='home'),
    path('', account_login, name='login'),
    path('register/', registration_view, name='register'),
    path('update/<int:pk>', edit_account_view, name='update'),
    path('logout/', signout, name='signout'),





    path('api/account/', include('accounts.api.urls', 'accounts_api')),
    path('api/home/', include('home.api.urls', namespace='home_api')),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('home.urls', namespace='home')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



