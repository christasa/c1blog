# _*_coding:utf-8_*_

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy

from .models import Blog_contant
from .views import auth


# Set your Rss
class BlogRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = auth['username']
    # 通过聚合阅读器跳转到网站的地址
    link = ""
    # 显示在聚合阅读器上的描述信息
    description = ""
    url = reverse_lazy('rss')

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
        return reverse_lazy('detail', kwargs={'id': item.id})
