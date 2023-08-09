from django.contrib import admin

from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author')
    empty_value_display = '-пусто-'


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'pub_date', 'blog')
    list_filter = ('pub_date', 'blog')
    empty_value_display = '-пусто-'


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'blog')
    list_filter = ('user', 'blog')
    empty_value_display = '-пусто-'


@admin.register(models.ReadStatus)
class ReadStatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'reader', 'post', 'status')
    empty_value_display = '-пусто-'
