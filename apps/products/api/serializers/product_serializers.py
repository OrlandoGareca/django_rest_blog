from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer
from apps.products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    # PRIMER METODO muestra todo los datos
    # menasure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()
    # SEGUNDO METODO muesta solo los datos del __str__ del modelo
    # menasure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        # include = ('id','desciption','photo_url','menasure_unit','category_product')

    # TERCER METODO representar los que necesitemos
    def to_representation(self, instance):
        request = self.context.get('request')
        if instance.image != '':
            photo_url = instance.image.url
            image = request.build_absolute_uri(photo_url)
        else:
            image = 'http://127.0.0.1:8000/static/img/empty.png'
        return {
            'id': instance.id,
            'name':instance.name,
            'desciption': instance.desciption,
            'image': image,
            # 'image': instance.image.url if instance.image != '' else "",
            'menasure_unit': instance.menasure_unit.desciption,
            'category_product': instance.category_product.descripcion,
        }
    # def get_photo_url(self, product):
    #     request = self.context.get('request')
    #     photo_url = product.image.url
    #     return request.build_absolute_uri(photo_url)
    # def get_photo_url(self, car):
    #     request = self.context.get('request')
    #     if photo and hasattr(photo, 'url'):
    #         photo_url = car.photo.url
    #         return request.build_absolute_uri(photo_url)
    #     else:
    #         return None


class ProductSerializerList(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True,allow_null=True)

    class Meta:
        model = Product
        fields = ('name', 'desciption', 'image', 'menasure_unit', 'category_product')
