# Generated by Django 4.1.2 on 2022-11-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PopularOpticsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('frame', models.CharField(blank=True, max_length=100, null=True)),
                ('lens', models.CharField(blank=True, max_length=100, null=True)),
                ('rate', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles')),
            ],
        ),
    ]
