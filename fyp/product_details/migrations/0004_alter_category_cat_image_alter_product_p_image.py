# Generated by Django 4.1.7 on 2023-04-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_details', '0003_alter_category_cat_image_alter_product_p_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(upload_to='cat_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
