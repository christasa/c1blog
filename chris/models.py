# _*_ coding: utf-8 _*_

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogType(models.Model):
    """博客类型"""
    type_name= models.CharField(max_length=15)
    def __unicode__(self):
        return self.type_name

    # 返回一个种下拉菜单的名字中的名字
    def __str__(self):
        return self.type_name

class Blog_contant(models.Model):
    """博客总内容"""
    id = models.AutoField(primary_key = True)  # 建立博客了id，便于数据库的查找
    title=models.CharField(max_length=100)
    blog_type=models.ForeignKey(BlogType,on_delete=None)   # 博客类型
    #content=RichTextField()          # 博客内容
    content =  RichTextUploadingField()
    author=models.ForeignKey(User,on_delete=None)    # 博客作者
    abstract = models.TextField()    # 博客摘要
    datetime = models.DateTimeField()   # 博客时间
    def __unicode__(self):
        return self.title
    class Meta:    # 按时间降序
        ordering = ['-datetime']
        # unique_together = ('url', 'title', 'datetime')



class Task(models.Model):
    dates = models.DateTimeField(null=False)
    submits = models.CharField(max_length=100,null=False)
    """任务视图的单表"""
    pass

class UserFile(models.Model):
    """用户的具体信息"""
    pass



