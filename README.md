# Blog

<details><summary>Russian language</summary>

## Описание проекта
Проект предусматривает сеть персональных блогов пользователей, в которой:

(1) каждый пользователь, созданный администратором из базы данных, имеет свой персональный блог  
(2) каждый пользователь может публиковать в своем блоге посты - элементарные записи с заголовком и кратким текстом, не превышающим 140 символов  
(3) каждый пользователь может подписываться на блоги других пользователей (без ограничений по количеству), чтобы следить за их публикациями, а также отписываться от них  
(4) каждый пользователь имеет свою ленту новостей, где отображаются посты из блогов, на которые он подписан, в порядке добавления постов (лента ограничена 500 постами с пагинацией по 10 постов)  
(5) каждый пользователь может отмечать посты в ленте как прочитанные, поддерживая актуальность информации в ленте  
(6) каждый пользователь может удалять свои посты, в этом случае лента других пользователей изменится (как и в случае с добавлением новых постов)  
(7) каждый пользователь раз в сутки получает подборку из 5 последних постов своих подписок  

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
cd Blog/
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
cd infra/
```
```
docker compose up -d
```
4. Создать администратора
```
docker compose exec app poetry run python manage.py createsuperuser
```
5. Заполнить БД случайными данными
```
команда fillbase <кол-во создаваемых пользователей>
```

```
docker compose exec app poetry run python manage.py fillbase 10
```

После запуска появится доступ к:
* [Документации](http://127.0.0.1/redoc/)
* [Админке django](http://127.0.0.1/admin/)
* [Админке postgres](http://127.0.0.1/adminer/)
* [Flower](http://127.0.0.1:5555/)
</details>

<details><summary>English language</summary>

## Project Description
The project envisages a network of users' personal blogs in which:

(1) each user created by the administrator from the database has his/her own personal blog  
(2) each user can publish posts on his/her blog - elementary entries with a title and a short text not exceeding 140 characters  
(3) each user can subscribe to the blogs of other users (with no limit on the number) to follow their publications, as well as unsubscribe from them  
(4) each user has their own news feed, which displays posts from the blogs they are subscribed to, in the order in which the posts were added (the feed is limited to 500 posts with pagination of 10 posts)  
(5) each user can mark posts in the feed as read, keeping the information in the feed up to date  
(6) each user can delete their own posts, in which case the feed of other users will change (as in the case of adding new posts)  
(7) each user receives a selection of the 5 latest posts of their subscriptions once a day  

## Technologies

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

## Project launch

1. Clone the repository and navigate to it on the command line
```
git clone git@github.com:avnosov3/Blog.git
```
```
cd Blog/
```
2. Create an .env file

```
DJANGO_KEY=<Specify secret key>
DEBUG=True (if launching in production mode, the variable must be deleted)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=network
POSTGRES_USER=<Specify username>
POSTGRES_PASSWORD=<Specify user password>
DB_HOST=db
DB_PORT=5432
REDIS_HOST=redis
```

3. Run docker compose
```
cd infra/
```
```
docker compose up -d
```
4. Create an administrator
```
docker compose exec app poetry run python manage.py createsuperuser
```
5. Fill the database with random data
```
command fillbase <number of users to be created>
```

```
docker compose exec app poetry run python manage.py fillbase 10
```

Once launched, there will be access to:
* [Documentation](http://127.0.0.1/redoc/)
* [Admin-panel django](http://127.0.0.1/admin/)
* [Admin-panel postgres](http://127.0.0.1/adminer/)
* [Flower](http://127.0.0.1:5555/)
</details>
