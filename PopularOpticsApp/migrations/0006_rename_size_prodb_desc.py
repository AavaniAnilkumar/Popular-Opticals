# Generated by Django 4.1.2 on 2022-12-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0005_rename_desc_prodb_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodb',
            old_name='size',
            new_name='desc',
        ),
    ]