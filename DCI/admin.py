from django.contrib import admin
from .models import DCI, DCIGroup, DCIItem

# Register your models here.
admin.site.register(DCI)
admin.site.register(DCIGroup)
admin.site.register(DCIItem)
