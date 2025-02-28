from rest_framework import serializers

from MyApps.models import Scanner, Product, Finding

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