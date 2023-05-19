from django.db import models


class Contacts(models.Model):
    title = models.CharField('Имя сотрудника', max_length=69)
    description = models.TextField('Краткое описание', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    password = models.CharField('Код', max_length=100, default='')
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['title']
