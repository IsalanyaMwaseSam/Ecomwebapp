# Generated by Django 4.0.4 on 2022-05-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0008_rename_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F', 'Fashion'), ('El', 'Electronics'), ('HB', 'Health & Beauty'), ('G', 'Gardening'), ('SP', 'Sports'), ('HO', 'Home & Office')], max_length=2, null=True),
        ),
    ]
