from django.db import models
import datetime

class Finding(models.Model):
    title = models.CharField(max_length=20, blank=False)
    line_number = models.IntegerField(blank=False)
    file_path = models.CharField(max_length=20, blank=False)
    mitigate_before = models.DateTimeField(blank=False)
    mitigation_violated = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=20, blank=False)
    business_criticality = models.IntegerField(blank=False)
    def __str__(self):
        return self.title

class Scanner(models.Model):
    title = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.title
