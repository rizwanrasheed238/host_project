# Generated by Django 4.1.7 on 2023-05-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiqueapp', '0020_product_is_deal_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='approved_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superadmin',
            field=models.BooleanField(default=True),
        ),
    ]
