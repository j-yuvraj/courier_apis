from django.contrib import admin
from .models import Package_Category,Package_Sizes

# Register your models here.
admin.site.register(Package_Category)
admin.site.register(Package_Sizes)