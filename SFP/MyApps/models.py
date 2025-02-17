from django.db import models
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

class Scanner(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=20)
    business_criticality = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return self.title

class Finding(models.Model):
    title = models.CharField(max_length=20)
    line_number = models.IntegerField()
    file_path = models.CharField(max_length=20)
    mitigate_before = models.DateField()
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    @property
    def mitigation_violated(self):
        return self.mitigate_before < datetime.datetime.now()

    def __str__(self):
        return self.title



