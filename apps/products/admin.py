from django.contrib import admin

# Register your models here.
# from apps.products.models import *

# from django_rest_blog.apps.products.models import MeasureUnit, CategoryProduct, Indicator, Product
from apps.products.models import *


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'desciption')


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')


admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product)
