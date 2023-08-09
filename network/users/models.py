from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username, email, password, **extra_fields)
        from blogs.models import Blog
        if not Blog.objects.filter(author=user).exists():
            Blog.objects.create(author=user)
        return user


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
            from blogs.models import Blog
            Blog.objects.create(author=self)
        else:
            super().save(*args, **kwargs)
