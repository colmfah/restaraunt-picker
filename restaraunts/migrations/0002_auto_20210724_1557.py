# Generated by Django 3.2 on 2021-07-24 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='restaraunt',
            name='image',
        ),
        migrations.RemoveField(
            model_name='restaraunt',
            name='rating',
        ),
    ]
