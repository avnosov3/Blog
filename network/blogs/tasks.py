from api.constants import FEED_CACHE_PATH
from blogs.models import Post
from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail

from .constatns import EMAIL_FEED_LIMITS
from users.models import CustomUser


@shared_task
def send_daily_feed_email(user_id):
    user = CustomUser.objects.get(pk=user_id)
    cache_key = FEED_CACHE_PATH.format(user.id)
    cached_queryset = cache.get(cache_key)

    if not cached_queryset:
        queryset = Post.objects.filter(
            blog__followers__user=user
        )[:EMAIL_FEED_LIMITS]
    else:
        queryset = cached_queryset
    if not queryset:
        return

    message = '\n\n'.join([
        (
            f'Название: {post.title}\n'
            f'Текст поста: {post.text}\n'
            f"Дата публикации: {post.pub_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f'Блог: {post.blog}'
        ) for post in queryset
    ])

    if message:
        send_mail(
            'Ваша новостная лента',
            message,
            'network@bk.ru',
            [user.email],
            fail_silently=False,
        )


@shared_task
def send_daily_feed_to_all_users():
    for user in CustomUser.objects.all():
        send_daily_feed_email.delay(user.id)
