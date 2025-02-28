from rest_framework import generics, viewsets

from MyApps.models import Scanner, Product, Finding
from MyApps.serializers import ScannerSerializer, ProductSerializer, FindingSerializer

class ScannerViewSet(viewsets.ModelViewSet):
    queryset = Scanner.objects.all()
    serializer_class = ScannerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FindingViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
