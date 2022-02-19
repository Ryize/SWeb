# SWeb

Online store template. Implemented registration, authorization, filters, adding / deleting goods, API, admin panel.

## Deploy locally:

Clone the repository and go to installed folder
```
git clone https://github.com/Ryize/SWeb.git
cd SWeb
```

Install requirements
```
pip3 install -r requirements.txt
```
> If you are deploying a project to a server or hosting with a domain, then specify it in the project settings in the ALLOWED_HOSTS(DjangoBlog.settings) variable
```
ALLOWED_HOSTS = ['127.0.0.1']
```

> If the DEBUG mode is disabled(False), the site will stop automatically collecting statics and media, do not forget to configure Nginx/Apache
```
DEBUG = True
```

Collect statics and run migrations
```
python3 manage.py collectstatic
python3 manage.py migrate
```

Run the website
```
python3 manage.py runserver
```

> Technologies used in the project: Python 3, Django, djangorestapi.
