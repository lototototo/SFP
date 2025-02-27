from itertools import product
from logging import raiseExceptions

from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from MyApps.models import Scanner
from MyApps.serializers import ScannerSerializer

from MyApps.models import Product
from MyApps.serializers import ProductSerializer

from MyApps.models import Finding
from MyApps.serializers import FindingSerializer

class ScannerAPIView(viewsets.ModelViewSet):
    queryset = Scanner.objects.all()
    serializer_class = ScannerSerializer

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FindingAPIView(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer
