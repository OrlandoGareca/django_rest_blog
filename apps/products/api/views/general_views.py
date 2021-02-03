from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, \
    CategoryProductSerializer


# class MeasureUnitListAPIView(generics.ListAPIView):
#     serializer_class = MeasureUnitSerializer
#
#     def get_queryset(self):
#         return MeasureUnit.objects.filter(state=True)

# class MeasureUnitListAPIView(generics.ListAPIView):
class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
