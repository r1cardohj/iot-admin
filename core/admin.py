from django.contrib import admin
from core.models import Property

# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
