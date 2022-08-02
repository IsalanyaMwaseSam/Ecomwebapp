# Generated by Django 4.0.4 on 2022-07-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_seller_account_is_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='Address_1',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='Address_2',
            new_name='Town',
        ),
        migrations.AddField(
            model_name='account',
            name='phonenumber',
            field=models.IntegerField(null=True, verbose_name='phonenumber'),
        ),
    ]
