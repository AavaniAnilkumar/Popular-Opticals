# Generated by Django 4.1.2 on 2022-12-29 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0004_prodb_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodb',
            old_name='desc',
            new_name='size',
        ),
    ]