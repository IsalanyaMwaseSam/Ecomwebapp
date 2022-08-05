# Generated by Django 4.0.4 on 2022-07-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('F', 'Fashion'), ('El', 'Electronics'), ('HB', 'Health & Beauty'), ('G', 'Gardening'), ('SP', 'Sports'), ('HO', 'Home & Office')], max_length=2, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('characteristics', models.TextField(max_length=3000, null=True)),
                ('description', models.TextField(max_length=3000, null=True)),
                ('specifications', models.TextField(max_length=3000, null=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]