# Generated by Django 4.0.2 on 2022-04-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_alter_orderproduct_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='ordered_date',
        ),
    ]