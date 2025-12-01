from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.AdminPerson)
class AdminPersonAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
