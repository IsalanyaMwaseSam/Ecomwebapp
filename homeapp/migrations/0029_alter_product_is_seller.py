# Generated by Django 4.0.4 on 2022-05-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0028_remove_billing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_seller',
            field=models.BooleanField(blank=True, max_length=200, null=True),
        ),
    ]
