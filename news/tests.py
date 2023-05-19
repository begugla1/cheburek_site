from django.template.defaultfilters import slugify
from django.test import TestCase
from datetime import datetime
from transliterate import translit


def default_datetime():
    return datetime.now()


def my_slugify(text):
    return slugify(translit(text, 'ru', reversed=True))
