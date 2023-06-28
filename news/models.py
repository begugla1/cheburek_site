from django.db import models
from django.urls import reverse
from . import tests


class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    anons = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', default=tests.default_datetime)
    is_published = models.BooleanField('Опубликовано', default=True)
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'cat_slug': self.cat.slug, 'art_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = tests.my_slugify(self.title)
        self.date = tests.default_datetime()
        super(Articles, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date', 'title']


class Category(models.Model):
    name = models.CharField('Название', max_length=50, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

