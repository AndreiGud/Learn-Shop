"""
URL configuration for ShopLearn project.

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
from django.contrib import admin
from django.urls import path
from ShopApp import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('PageUrl_2', views.PageUrl_2),
    path('PageUrl_3', views.PageUrl_3),
    path('PageUrl_4', views.PageUrl_4),
    path('PageUrl_5', views.PageUrl_5),
    path('Login', views.Login),
    path('Account', views.Account_User),
    path('admin/', admin.site.urls),
]
