# Generated by Django 4.0.4 on 2022-05-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0020_alter_product_discount_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
