from django.contrib import admin
from .models import Parameter


# Register your models here.
@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'time')