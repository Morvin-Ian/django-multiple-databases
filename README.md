# django-multiple-database

1: Configure the Databases
    In your Django project's settings.py file, define the configurations for your multiple databases. 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'default_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '',
        },
        'second_db': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'second_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

2: Create Database Router
    Next, you need to create a database router to handle the database routing logic. The router determines which database to use for each database operation. 

class MultiDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'second_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'your_app_label':
            return 'second_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db1 = getattr(obj1, "_state").db
        db2 = getattr(obj2, "_state").db
        if db1 == 'second_db' or db2 == 'second_db':
            return True
        return db1 == db2

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'your_app_label':
            return db == 'second_db'
        return db == 'default'

3: Configure Database Router in Settings

    DATABASE_ROUTERS = ['project_name.routers.MultiDBRouter']
