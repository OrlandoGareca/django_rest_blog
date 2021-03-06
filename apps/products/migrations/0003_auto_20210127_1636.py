# Generated by Django 3.1.5 on 2021-01-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210127_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del Producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto'),
        ),
    ]
