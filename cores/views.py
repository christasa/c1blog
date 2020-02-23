from django.shortcuts import render
from django.core.paginator import  Paginator
from .models import Blog_contant,BlogType,Project,AboutMe,Friends
# Create your views here.

auth={}
auth['username'] = 'name'
auth['userimgpath'] = '/static/img/user.jpg'
auth['motto'] = 'moto'
auth['github'] = '# '


def index(request):
    """首页"""
    global auth
    project = Project.objects.all()   # 首页博客信息
    return render(request,'index.html',{'pro':project,
                                        'auth':auth})

def blog(request,type=None):
    """博客面展示"""
    global auth
    page_num = request.GET.get('page', 1)
    if type:
        blog_all_list = Blog_contant.objects.filter(blog_type = type)
    else:
        blog_all_list = Blog_contant.objects.all()

    if request.method == "POST":
        query = request.POST.get('search')
        if query:
            blog_all_list = Blog_contant.objects.filter(author__blog_contant__title__icontains = query)
    paginator = Paginator(blog_all_list,6)  # 每10页进行分页
    page_of_blogs = paginator.get_page(page_num)
    project = Project.objects.all()
    total=Blog_contant.objects.all().count()   # 计算博客的总数
    page_nums = page_of_blogs.number #获取当前页码
    # 将博客的分类以及数量都打印出来
    Type_all=[]
    for blogtype in BlogType.objects.all():
        Types = {}          # 对传入的参数进行适配
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'blog.html',{'Them':page_of_blogs,
                                       'totals':total,
                                       'types':Type_all,
                                       'pro':project,
                                       'auth':auth})

def DetailBlog(request,id):
    '''Detail of blog'''
    global auth
    blogDetail = Blog_contant.objects.get(id=id)  # 定位到当前博客的位置
    project = Project.objects.all()
    all_blog = Blog_contant.objects.all()
    Type_all = []
    # True the page
    try:
        preblog = Blog_contant.objects.get(id=id-1)
    except:preblog=None
    try:
        nextblog = Blog_contant.objects.get(id=id+1)
    except:nextblog=None
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'cons.html',{'Thme':blogDetail,
                                       'side_in':all_blog,
                                       'types':Type_all,
                                       'pro':project,
                                       'auth':auth,
                                       'pre':preblog,
                                       'next':nextblog})


def List(request):
    """"所有博客列表"""
    global auth
    all_blog = Blog_contant.objects.all()
    project = Project.objects.all()
    Type_all = []
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request,'lists.html',{'AllBlog':all_blog,
                                        'types':Type_all,
                                        'pro':project,
                                        'auth':auth})

def about(request):
    '''About me'''
    global auth
    project = Project.objects.all()
    Type_all = []
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    about = AboutMe.objects.all()
    return render(request,'about.html',{'types':Type_all,
                                        'pro':project,
                                        'auth':auth,
                                        'about':about})


def friend(request):
    """Friends """
    global auth
    all_friends = Friends.objects.all()
    project = Project.objects.all()
    Type_all = []
    for blogtype in BlogType.objects.all():
        Types = {}
        Types['type'] = blogtype
        Types['type_count'] = Blog_contant.objects.filter(blog_type=blogtype).count()
        Types['type_id'] = blogtype.id
        Type_all.append(Types)
    return render(request, 'friends.html', {'types': Type_all,
                                            'pro': project,
                                            'fre': all_friends,
                                            'auth': auth})