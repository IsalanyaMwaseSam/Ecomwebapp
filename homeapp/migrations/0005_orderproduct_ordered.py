# Generated by Django 4.0.2 on 2022-04-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_orderproduct_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]