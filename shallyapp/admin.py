from django.contrib import admin
from .models import SensorData, waterlevel

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at', 'water','temp',)  # Fields to display in the admin list view
    search_fields = ('value','water','temp',)  # Fields to search in the admin interface
    list_filter = ('created_at','water','temp',)  # Fields to filter by in the admin list view
    fields = ('value','water','temp',)  # Add 'value' field to the admin form


admin.site.register(SensorData, SensorDataAdmin)

