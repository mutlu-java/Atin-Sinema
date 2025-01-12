# Generated by Django 5.1 on 2024-10-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_movie_actors_movie_director_movie_imdb_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(default='Unknown Category', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenwriters',
            field=models.TextField(default='Unknown Screenwriters'),
        ),
    ]
