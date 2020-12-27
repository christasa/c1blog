from django.contrib import admin

from cores import models

# Register your models here.


# Display of blog
class BlogShow(admin.ModelAdmin):
    list_display = ('id', 'title', 'datetime')
    list_display_links = ('title', )


# Display of administrator
class TypeShow(admin.ModelAdmin):
    list_display = ('type_name', )


class ProjectsShow(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'url')


class FriendShow(admin.ModelAdmin):
    list_display = ('name', 'url')


admin.site.register(models.Blog_contant, BlogShow)
admin.site.register(models.BlogType, TypeShow)
admin.site.register(models.Project, ProjectsShow)
admin.site.register(models.AboutMe)
admin.site.register(models.Friends, FriendShow)
