from django.contrib import admin
from MyApps.models import Finding, Scanner, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class FindingResource(resources.ModelResource):
    class Meta:
        model = Finding

class FindingAdmin(ImportExportModelAdmin):
    resource_class = FindingResource

admin.site.register(Finding, FindingAdmin)
admin.site.register(Scanner)
admin.site.register(Product)