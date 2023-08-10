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

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        is_new_user = not self.pk
        super().save(*args, **kwargs)

        if is_new_user and not self.is_superuser:
            from blogs.models import Blog
            if not Blog.objects.filter(author=self).exists():
                Blog.objects.create(author=self)
