# Generated by Django 2.1.5 on 2021-04-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='averageRating',
            field=models.FloatField(default=0),
        ),
    ]
