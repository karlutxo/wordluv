# Generated by Django 4.1 on 2022-09-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordluv_app', '0003_word_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]