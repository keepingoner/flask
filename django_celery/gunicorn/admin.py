from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import TestModel


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    pass
