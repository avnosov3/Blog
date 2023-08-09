from django.contrib import admin

from .models import Blog, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date', 'blog')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
