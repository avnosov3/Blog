from django.db import models

from . import constatns
from users.models import CustomUser


class Blog(models.Model):
    author = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='blog',
        verbose_name='Автор',
        help_text='Введите автора блога',
    )

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'Автор блога "{self.author.get_username()}"'


class Post(models.Model):
    title = models.CharField(
        max_length=constatns.TITLE_LENGTH,
        verbose_name='Название',
        help_text='Введите название поста',
    )
    text = models.TextField(
        max_length=constatns.TEXT_LENGTH,
        verbose_name='Текст поста',
        help_text='Введите текст поста',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Блог',
        help_text='Блог, к которому относится пост'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    OUT = (
        '"{title}" '
        '"{text:.15}" '
        '"{pub_date}" '
        '"{blog}" '
    )

    def __str__(self):
        return self.OUT.format(
            title=self.title,
            text=self.text,
            pub_date=self.pub_date,
            blog=self.blog.author
        )


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Подписчик',
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Блог'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                name='Проверка повторной подписки',
                fields=['user', 'blog'],
            ),
        ]

    def __str__(self):
        return f'"{self.user}" подписан на {self.blog}'


class ReadStatus(models.Model):
    reader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='statuses',
        verbose_name='Читатель',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='statuses',
        verbose_name='Пост',
    )
    status = models.BooleanField(
        null=True,
        verbose_name='Статус прочтения поста'
    )

    class Meta:
        verbose_name = 'Статсу Прочтения'
        verbose_name_plural = 'Статусы Прочтения'
