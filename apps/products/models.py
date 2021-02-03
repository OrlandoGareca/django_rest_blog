from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords

# from django_rest_blog.apps.base.models import BaseModel
from apps.base.models import BaseModel
from django_rest_blog.settings import MEDIA_URL, STATIC_URL


class MeasureUnit(BaseModel):
    desciption = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidad de Medidas'

    def __str__(self):
        return self.desciption


class CategoryProduct(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de Productos'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.descripcion


class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_producto = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,
                                          verbose_name='Indicator de Ofertas')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        return f'Oferta de la categoria {self.category_producto}:{self.descount_value}%'


class Product(BaseModel):
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    desciption = models.TextField('Descripcion de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto',max_length=255, upload_to='products/',
                              blank=True, null=True,default='products/empty.png')
    menasure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,
                                         verbose_name='Categoria de Producto', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
