# Generated by Django 4.1.3 on 2023-05-08 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articles",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="get_articles",
                to="news.category",
                verbose_name="Категория",
            ),
        ),
    ]
