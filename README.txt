Let me explain it briefly.

1. languages/apps.py: declares LanguagesConfig class (subclass of django.apps.AppConfig) that represents Rest CRUD Apis app and its configuration.
2. api_example/settings.py: contains settings for our Django project: mydb Database engine, INSTALLED_APPS list with Django REST framework, Languages Application, CORS and MIDDLEWARE.
3. languages/models.py: defines Language, Paradigm, Programmer data model class (subclass of django.db.models.Model).
4. migrations/0001_initial.py: is created when we make migrations for the data model, and will be used for generating MySQL database table.
5. languages/serializers.py: manages serialization and deserialization with LanguageSerializer class (subclass of rest_framework.serializers.ModelSerializer).
6. languages/views.py: contains functions to process HTTP requests and produce HTTP responses (using LanguageSerializer).
7. languages/urls.py: defines URL patterns along with request functions in the Views.
8. api_example/urls.py: also has URL patterns that includes tutorials.urls, it is the root URL configurations.