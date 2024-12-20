# Generated by Django 5.1 on 2024-10-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_movie_title_alter_movie_iframe_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='Unknown Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='iframe_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.URLField(max_length=300),
        ),
    ]
