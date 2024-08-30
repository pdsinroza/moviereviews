# Generated by Django 5.0.6 on 2024-08-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='movies/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]