# Generated by Django 4.1 on 2022-09-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordluv_app', '0005_word_created_word_lastshown_word_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='lastshown',
            field=models.DateTimeField(null=True),
        ),
    ]
