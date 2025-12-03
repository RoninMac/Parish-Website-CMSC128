from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'created_at')