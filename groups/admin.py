from django.contrib import admin
from .models import ChurchGroups

@admin.register(ChurchGroups)
class ChurchGroupsAdmin(admin.ModelAdmin):
    list_display = ("name", "posted_by", "created_at")

    def save_model(self, request, obj, form, change):
        if not change:  # Only set on object creation
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)
