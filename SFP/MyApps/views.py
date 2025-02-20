from django.shortcuts import render
from .models import Finding
import json


def import_json(request):
    if request.method =='POST' and request.FILES['trufflehog3']:
        json_file = request.FILES['trufflehog3']
        data = json.load(json_file)
        for item in data:
            finding = Finding(
                title = 7,
                file_path = item['path'],
                line_number = item['line'],
                severity = item['rule']['severity']
            )
            finding.save()
