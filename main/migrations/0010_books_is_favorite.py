# Generated by Django 3.1.4 on 2021-01-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_books_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
