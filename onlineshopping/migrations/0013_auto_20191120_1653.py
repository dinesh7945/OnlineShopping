# Generated by Django 2.2.4 on 2019-11-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopping', '0012_auto_20191120_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.BigIntegerField(verbose_name=50),
        ),
    ]
