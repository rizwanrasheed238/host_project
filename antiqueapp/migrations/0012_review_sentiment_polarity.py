# Generated by Django 4.1.1 on 2023-03-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueapp', '0011_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentiment_polarity',
            field=models.FloatField(default=0.0),
        ),
    ]
