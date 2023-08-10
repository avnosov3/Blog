from random import sample

from blogs.models import Blog, Follow
from django.core.management.base import BaseCommand
from mixer.backend.django import mixer


class Command(BaseCommand):
    help = 'Заполняет модели случайными данными с использованием mixer'

    def add_arguments(self, parser):
        parser.add_argument(
            'num_users', type=int, help='Количество пользователей для создания'
        )

    def handle(self, *args, **options):
        num_users = options['num_users']
        users = [mixer.blend('users.CustomUser') for _ in range(num_users)]
        posts = [
            mixer.blend(
                'blogs.Post', blog=user.blog
            ) for user in users for _ in range(11)
        ]
        for user in users:
            not_followed_blogs = Blog.objects.exclude(followers__user=user)
            for blog in sample(list(not_followed_blogs), 3):
                Follow.objects.create(user=user, blog=blog)
        for user in users:
            for post in posts:
                mixer.blend(
                    'blogs.ReadStatus',
                    reader=user,
                    post=post,
                    status=mixer.RANDOM
                )
        self.stdout.write(self.style.SUCCESS('БД заполнена'))
