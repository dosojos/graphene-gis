import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "FAKE_KEY"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "django_test.sqlite",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    },
]

INSTALLED_APPS = [
    "graphene_django",
    "graphene_gis",
    "graphene_gis.tests",
]
GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal306"
# if os.name == "nt":
#     GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal306"
#     # GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal202'
