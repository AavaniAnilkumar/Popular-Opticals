# Generated by Django 4.1.2 on 2022-12-31 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0007_prodb_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminpgdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
