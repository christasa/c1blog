from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.core.paginator import  Paginator
from plugin import codes
import json
from .models import Blog_contant,BlogType
# Create your views here.

def index(request):
    """首页面展示"""
    page_num = request.GET.get('page', 1)
    blog_all_list = Blog_contant.objects.all()
    paginator = Paginator(blog_all_list,6)  # 每10页进行分页
    page_of_blogs = paginator.get_page(page_num)
    total=Blog_contant.objects.all().count()   # 计算博客的总数
    page_nums = page_of_blogs.number #获取但钱页码
    # 优化分页器
    page_range = [(page_nums+i) for i in range(-3,3) if paginator.num_pages>=(page_nums+i)>0]
    # 加上页面省略的配置
    if page_range[0]-1>=2:page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >=2:page_range.append('...')
    # 将第一页和最后一页放在翻页条中
    if page_range[0]!=1:page_range[0]=1
    if page_range[-1]!=paginator.num_pages:page_range[5]=paginator.num_pages
    Type_counts = BlogType.objects.all()
    return render(request,'index.html',{'Them':page_of_blogs,'totals':total,'side_in':blog_all_list,'types':Type_counts})


# 小工具中的base64编解码
def base64s(request):
    page_num = request.GET.get('page', 1)
    blog_all_list = Blog_contant.objects.all()
    paginator = Paginator(blog_all_list,6)  # 每10页进行分页
    page_of_blogs = paginator.get_page(page_num)
    total=Blog_contant.objects.all().count()   # 计算博客的总数
    ret = {'msg':None}
    if request.method =='POST':
        content = request.POST.get('con')
        if len(content)>1000:
            return render(request, 'tools/base64s.html', {'result': '错误!','totals':total,'side_in':blog_all_list})
        try:
            # 过滤掉可能的命令执行行
            content = content.replace('&','#')
            content = content.replace('|','#')
        except:
            pass
        # if 'decode' in request.POST:
        if request.POST['type'] == 'decode':
            result = codes.decode(content)
            ret['msg'] = result
            return HttpResponse(json.dumps(ret))
        else:
            result = codes.encode(content)
            result = result.decode('utf-8')
            ret['msg'] = result
            return HttpResponse(json.dumps(ret))

    else:
        return render(request, 'tools/base64s.html',{'totals':total,'side_in':blog_all_list})


def htmcode(request):
    page_num = request.GET.get('page', 1)
    blog_all_list = Blog_contant.objects.all()
    paginator = Paginator(blog_all_list, 6)  # 每10页进行分页
    total = Blog_contant.objects.all().count()  # 计算博客的总数
    ret = {'msg': None}
    if request.method == 'POST':
        content = request.POST.get('con')
        if len(content) > 1000:
            return render(request, 'tools/hmcode.html', {'result': '错误!', 'totals': total, 'side_in': blog_all_list})
        try:
            # 过滤掉可能的命令执行行
            content = content.replace('&&', '#')
            content = content.replace('|', '#')
        except:
            pass
        # if 'decode' in request.POST:
        if request.POST['type'] == 'decode':
            result = codes.htmldecode(content)
            ret['msg'] = result
            return HttpResponse(json.dumps(ret))
        else:
            result = codes.htmlcode(content)
            # result = result.decode('utf-8')
            ret['msg'] = result
            return HttpResponse(json.dumps(ret))
    else:
        return render(request, 'tools/hmcode.html', {'totals': total, 'side_in': blog_all_list})
def DetailBlog(request,id):
    '''每一页的博客的详细内容'''
    blogDetail = Blog_contant.objects.get(id=id)  # 定位到当前博客的位置
    all_blog = Blog_contant.objects.all()
    Type_counts = BlogType.objects.all()
    return render(request,'cons.html',{'Thme':blogDetail,'side_in':all_blog,'types':Type_counts})

def List(request):
    all_blog = Blog_contant.objects.all()
    Type_counts = BlogType.objects.all()
    return render(request,'lists.html',{'AllBlog':all_blog,'types':Type_counts})
