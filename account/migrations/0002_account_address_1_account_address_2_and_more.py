# Generated by Django 4.0.2 on 2022-02-18 16:44

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Address_1',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='Address_2',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=60, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='account',
            name='other_names',
            field=models.CharField(max_length=200, null=True, verbose_name='other_names'),
        ),
    ]
