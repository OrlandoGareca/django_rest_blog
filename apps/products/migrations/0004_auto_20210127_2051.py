# Generated by Django 3.1.5 on 2021-01-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210127_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto'),
        ),
    ]
