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
from django.urls import re_path
from ShopApp import views

urlpatterns = [
    re_path(r'^$', views.indexListView.as_view(), name="index"),
    re_path(r"^catalog/$", views.CatalogListView.as_view(), name="catalog"),
    path('books/', views.CatalogListViewN.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.CatalogListViewN.as_view(), name='booksn'),
    re_path(r'^PageUrl_3', views.PageUrl_3, name="PageUrl_3"),
    re_path(r'^PageUrl_4', views.PageUrl_4, name="PageUrl_4"),
    re_path(r'^PageUrl_5', views.PageUrl_5, name="PageUrl_5"),
    re_path(r'^Login', views.Login, name="Login"),
    re_path(r'^Account', views.Account_User, name="Account_User"),
    path('admin/', admin.site.urls),
]
