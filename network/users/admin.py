from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'is_superuser')
    empty_value_display = '-пусто-'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data['password'])
            super().save_model(request, obj, form, change)
            from blogs.models import Blog
            if not Blog.objects.filter(author=obj).exists():
                Blog.objects.create(author=obj)
        else:
            super().save_model(request, obj, form, change)
