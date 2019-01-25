from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.core.paginator import  Paginator
from plugin import codes
import json
from .models import Blog_contant,BlogType,Project
from django.views.decorators.cache import cache_page, cache_control, never_cache
# Create your views here.


def index(request):
    project = Project.objects.all()   # 首页博客信息
    return render(request,'index.html',{'pro':project})


def blog(request,type=None):
    """首页面展示"""
    page_num = request.GET.get('page', 1)
    if type:
        blog_all_list = Blog_contant.objects.filter(blog_type = type)
    else:
        blog_all_list = Blog_contant.objects.all()
    paginator = Paginator(blog_all_list,6)  # 每10页进行分页
    page_of_blogs = paginator.get_page(page_num)
    # project = Project.objects.all()
    total=Blog_contant.objects.all().count()   # 计算博客的总数
    page_nums = page_of_blogs.number #获取但钱页码
    # 将博客的分类以及数量都打印出来
    Type_all=[]
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'blog.html',{'Them':page_of_blogs,'totals':total,'types':Type_all})

def DetailBlog(request,id):
    '''每一页的博客的详细内容'''
    blogDetail = Blog_contant.objects.get(id=id)  # 定位到当前博客的位置
    # project = Project.objects.all()
    all_blog = Blog_contant.objects.all()
    Type_all = []
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'cons.html',{'Thme':blogDetail,'side_in':all_blog,'types':Type_all})

def List(request):
    all_blog = Blog_contant.objects.all()
    # project = Project.objects.all()
    Type_all = []
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'lists.html',{'AllBlog':all_blog,'types':Type_all})
