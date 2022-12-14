# Generated by Django 3.2.16 on 2022-12-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourite_director',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourite_genre',
            field=models.CharField(blank=True, choices=[('NP', 'No Preference'), ('ACT', 'Action'), ('ADV', 'Adventure'), ('COM', 'Comedy'), ('CRI', 'Crime'), ('DRA', 'Drama'), ('FAM', 'Family'), ('FAN', 'Fantasy'), ('HOR', 'Horror'), ('MUS', 'Music'), ('ROM', 'Romance'), ('SCI', 'Sci-Fi'), ('SPT', 'Sport'), ('SUP', 'Superhero'), ('THR', 'Thriller'), ('WAR', 'War'), ('WST', 'Western')], default='', max_length=50),
        ),
    ]
