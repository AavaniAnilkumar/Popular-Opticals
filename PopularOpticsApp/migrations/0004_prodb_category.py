# Generated by Django 4.1.2 on 2022-11-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0003_remove_prodb_lens'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodb',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]