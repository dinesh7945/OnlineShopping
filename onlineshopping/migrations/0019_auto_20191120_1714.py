# Generated by Django 2.2.4 on 2019-11-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopping', '0018_auto_20191120_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.PositiveIntegerField(),
        ),
    ]
