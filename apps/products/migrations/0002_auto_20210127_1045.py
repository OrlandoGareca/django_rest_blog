# Generated by Django 3.1.5 on 2021-01-27 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='menasure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='menasure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoria de Producto'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='menasure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoria de Producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='menasure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]
