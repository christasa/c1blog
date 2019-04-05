from django.contrib import admin
from chris import models
# Register your models here.

# 管理员编辑博客中的显示
class BlogShow(admin.ModelAdmin):
    list_display = ('id','title','datetime')
    list_display_links = ('title',)

# 管理员类型的显示
class TypeShow(admin.ModelAdmin):
    list_display = ('type_name',)

class ProjectsShow(admin.ModelAdmin):
    list_display = ('title','datetime','url')

admin.site.register(models.Blog_contant, BlogShow)
admin.site.register(models.BlogType,TypeShow)
admin.site.register(models.Project,ProjectsShow)
admin.site.register(models.AboutMe)