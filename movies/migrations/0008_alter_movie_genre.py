# Generated by Django 3.2.16 on 2022-12-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('drama', 'Drama'), ('family', 'Family'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('music', 'Music'), ('romance', 'Romance'), ('sci-Fi', 'Sci-Fi'), ('sport', 'Sport'), ('superhero', 'Superhero'), ('thriller', 'Thriller'), ('war', 'War'), ('western', 'Western')], default='', max_length=50),
        ),
    ]