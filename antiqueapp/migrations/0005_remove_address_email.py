# Generated by Django 4.1.1 on 2023-03-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueapp', '0004_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='email',
        ),
    ]