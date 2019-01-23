"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
#from Myblog import settings.STATIC_ROOT
from chris import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("_christa",admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index),
    path('tools/base64s/',views.base64s),
    path('tools/htmls/',views.htmcode),
    path(r'details/<int:id>/',views.DetailBlog,name='detail'),
    path(r'lists/',views.List),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
