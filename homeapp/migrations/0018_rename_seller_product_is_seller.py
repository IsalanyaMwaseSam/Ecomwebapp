# Generated by Django 4.0.4 on 2022-06-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0017_product_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='is_seller',
        ),
    ]
