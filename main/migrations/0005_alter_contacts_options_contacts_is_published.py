# Generated by Django 4.1.3 on 2023-05-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_contacts_password"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contacts",
            options={
                "ordering": ["title"],
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.AddField(
            model_name="contacts",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
    ]
