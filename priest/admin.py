from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Priest)
class PriestAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'photo', 'bio', 'posted_by')
    search_fields = ('name',)

    
    def save_model(self, request, obj, form, change):
        if not change:  # Only set on object creation
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)