from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Priest)
class PriestAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'photo', 'bio')
    search_fields = ('name',)