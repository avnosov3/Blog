from django.contrib import admin

from .models import Blog, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author')
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'pub_date', 'blog')
    list_filter = ('pub_date', 'blog')
    empty_value_display = '-пусто-'
