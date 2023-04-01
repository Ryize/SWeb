# SWeb

Шаблон интернет-магазина. Реализована регистрация, авторизация, фильтры, добавление/удаление товаров, API, админ-панель.
По мимо магазина в проекте есть небольшой блог.

## Прежде всего:

Клонируйте репозиторий и перейдите в установленную папку:
```
git clone https://github.com/Ryize/SWeb.git
cd SWeb
```

Установите requirements:
```
pip3 install -r requirements.txt
```
> Если вы развертываете проект на сервере или хостинге с доменом, то укажите это в настройках проекта в ALLOWED_HOSTS(DjangoBlog.settings) переменная
```
ALLOWED_HOSTS = ['127.0.0.1']
```

> Если режим DEBUG отключен (False), сайт перестанет автоматически собирать статику и медиа, не забудьте сконфигурировать Nginx/Apache
```
DEBUG = True
```

Соберите statics и выполните migrations:
```
python3 manage.py collectstatic
python3 manage.py migrate
```

Запустите проект:
```
python3 manage.py runserver
```

> Технологии используемые в проекте: Python 3, Django, djangorestapi.
