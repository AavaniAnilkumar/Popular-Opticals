# Generated by Django 4.1.2 on 2022-11-29 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0002_prodb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodb',
            name='lens',
        ),
    ]
