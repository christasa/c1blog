"""c1blog URL Configuration

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
from cores import views
from cores.feeds import BlogRssFeed
from cores.sitemaps import sitemaps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index),
    path(r'blog/', views.blog, name='blog_list'),
    path(r'blog/<str:type>/', views.blog, name='blog'),
    path(r'details/<int:id>/', views.DetailBlog, name='detail'),
    path(r'friends/', views.friend, name='friend'),
    path(r'lists/', views.List, name='lists'),
    path(r'rss/', BlogRssFeed(), name='rss'),
    path(r'about/', views.about, name='about'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
