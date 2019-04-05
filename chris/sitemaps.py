#_*_coding:utf-8_*_
# _Author : Christa
# Date :2019/3/31 14:38
# FileName : sitemap.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
from .models import Blog_contant


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        # 静态url的name
        return ['index', 'blog_list','lists' ,'rss']

    def location(self, item):
        return reverse_lazy(item)


class BlogSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Blog_contant.objects.all().order_by('-id')

    def location(self, item):
        return reverse_lazy('detail', kwargs={'id': item.id})


sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}
