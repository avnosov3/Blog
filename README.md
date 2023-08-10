## Описание проекта
Каждый пользователь имеет свой персональный блог, в котором он может публиковать посты. Важно отметить следующие ключевые возможности:
1. Администратор создаёт пользователей. При создании пользователя автоматически создается персональный блог.
2. Пользователи могут публиковать элементарные записи с заголовком и кратким текстом, не превышающим 140 символов.
3. Пользователи могут подписываться на блоги других пользователей, следя за их публикациями.
4. Каждый пользователь имеет свою ленту новостей, где отображаются посты из блогов, на которые он подписан. Лента ограничена 500 постами, с пагинацией по 10 постов.
5. Пользователи могут отмечать посты в ленте как прочитанные, поддерживая актуальность информации.
6. Пользователи получают раз в сутки подборку из 5 последних постов своих подписок.

## Техно-стек

* python 3.10
* django 3.2.20
* drf 3.14.0
* gunicorn 21.2.0
* postgres 14.0
* psycopg2-binary 2.9.7
* nginx 1.19.3
* django-redis 5.3.0
* celery 5.3.1
* flower 2.0.0
* docker 20.10.16
* docker-compose 3.8

## Запуск проекта

1. Клонировать репозиторий и перейти в него в командной строке
```
git clone git@github.com:avnosov3/Blog.git
```
```
cd Blog
```
2. Создать файл .env

```
DJANGO_KEY=<Указать секретный ключ>
DEBUG=True (если запуск в боевом режиме, то необходимо удалить переменную)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=network
POSTGRES_USER=<Указать имя пользователя>
POSTGRES_PASSWORD=<Указать пароль пользователя>
DB_HOST=db
DB_PORT=5432
REDIS_HOST=redis
```

3. Запустить docker compose
```
docker compose up -d
```
4. Создать администратора
```
docker compose exec app poetry run python manage.py createsuperuser
```
5. Заполнить БД случайными данным
```
команда fillbase <кол-во создаваемых пользователей>
```

```
docker compose exec app poetry run python manage.py fillbase 10
```

После запуска появится доступ к:
* [Документации](http://127.0.0.1/redoc/)
* [Админке postgres](http://127.0.0.1/adminer/)
* [Flower](http://127.0.0.1:5555/)
