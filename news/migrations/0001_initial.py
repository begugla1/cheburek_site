# Generated by Django 4.1.3 on 2023-05-08 09:35

from django.db import migrations, models
import django.db.models.deletion
import news.tests


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Articles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                ("anons", models.CharField(max_length=200, verbose_name="Анонс")),
                ("full_text", models.TextField(verbose_name="Статья")),
                (
                    "date",
                    models.DateTimeField(
                        default=news.tests.default_datetime,
                        verbose_name="Дата публикации",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="news.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["-date", "title"],
            },
        ),
    ]
