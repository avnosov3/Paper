# paper

# Запуск проекта

Проект можно запустить через docker или скачать репозиторий с github

Чтобы было удобнее посмотреть способ формирования дайджеста, после запуска нужно дёрнуть [ручку](http://127.0.0.1:8000/api/v1/auto/fill-db), которая заполнит БД

# Через Docker

Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:avnosov3/paper.git
cd paper/
```

Создать .env и заполнить

```
DB_ENGINE=postgresql+asyncpg
POSTGRES_DB=paper
POSTGRES_USER=<Указать имя пользователя>
POSTGRES_PASSWORD=<Указать пароль пользователя>
DB_HOST=db
DB_PORT=5432
FASTAPI_USERS_SECRET=<Указать секрет>
```

Запустить docker compose

```
docker compose up -d
```

Провести миграции

```
docker compose exec paper poetry run alembic upgrade head
```

Чтобы было удобнее посмотреть способ формирования дайджеста, после запуска нужно дёрнуть [ручку](http://127.0.0.1:8000/api/v1/auto/fill-db), которая заполнит БД


Сформировать дайджест

```
POST запрос на http://127.0.0.1:8000/api/v1/digest/{USER_ID}?likes_limits={УКАЗАТЬ МИНИМАЛЬНОЕ КОЛ-ВО ЛАЙКОВ В ПОСТАХ}
```

# Через GitHub

Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:avnosov3/paper.git
cd paper/
```

Установить зависимости

```
poetry install
```

Создать .env и заполнить

```
DB_ENGINE=postgresql+asyncpg
POSTGRES_DB=paper
POSTGRES_USER=<Указать имя пользователя>
POSTGRES_PASSWORD=<Указать пароль пользователя>
DB_HOST=localhost
DB_PORT=5432
FASTAPI_USERS_SECRET=<Указать секрет>
```

Провести миграции
```
poetry run alembic upgrade head
```

Запустить проект

```
poetry run uvicorn app.main:app
```

Чтобы было удобнее посмотреть способ формирования дайджеста, после запуска нужно дёрнуть [ручку](http://127.0.0.1:8000/api/v1/auto/fill-db), которая заполнит БД


Сформировать дайджест

```
POST запрос на http://127.0.0.1:8000/api/v1/digest/{USER_ID}?likes_limits={УКАЗАТЬ МИНИМАЛЬНОЕ КОЛ-ВО ЛАЙКОВ В ПОСТАХ}
```


# Документация

После запуска документация будет доступна в виде
* [swagger](http://127.0.0.1:8000/docs/)
* [redoc](http://127.0.0.1:8000/redoc/)

# Доступ к админке postgres

Админка будет доступна только при работе через Docker

* [adminer](http://127.0.0.1:8080/)