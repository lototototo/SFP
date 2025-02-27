from rest_framework import serializers
from django.core.validators import MinValueValidator,MaxValueValidator

from MyApps.models import Scanner
from MyApps.models import Product
from MyApps.models import Finding


class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanner
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = ('__all__')