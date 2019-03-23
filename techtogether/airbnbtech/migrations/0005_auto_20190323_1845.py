# Generated by Django 2.1.7 on 2019-03-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnbtech', '0004_auto_20190323_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finallocation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='location',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
