"""
URL configuration for urlshortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# urlshortener/urls.py
from django.contrib import admin
from django.urls import path
from shortener.views import shorten, redirect_to_long_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shorten, name='shorten'),
    path('<str:short_code>/', redirect_to_long_url, name='redirect_to_long_url'),
]
