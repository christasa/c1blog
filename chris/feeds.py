#_*_coding:utf-8_*_
# _Author : Christa
# Date :2019/3/30 23:51
# FileName : feed.py

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Blog_contant


class BlogRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Blog of christa"
    # 通过聚合阅读器跳转到网站的地址
    link = "https://christa.top"
    # 显示在聚合阅读器上的描述信息
    description = "安全杂谈"
    url=reverse_lazy('rss')
    # 需要显示的内容条目
    def items(self):
        return Blog_contant.objects.all()
    # 聚合器中显示的内容条目的标题

    def item_title(self, item):
        return item.title

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.abstract

    def item_link(self, item):
        return reverse_lazy('detail',kwargs={'id':item.id})