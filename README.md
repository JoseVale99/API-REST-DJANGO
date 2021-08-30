# API REST WITH DJANGO



## INSTALL

```bash
pipenv install django
pipenv install djangorestframework
pipenv install django-cors-headers
pipenv install psycopg2
```

## SETTINGS IN DATABASE
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR NAME DB',
        'USER': 'YOUR USERNAME',
        'PASSWORD': 'YOUR PASSWORD',
        'HOST': 'YOUR HOST/ localhost',
        'PORT': '5432'
    }
}
```


