# Generated by Django 4.0.4 on 2022-05-31 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0030_alter_product_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_seller',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
