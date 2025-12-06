from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ( 'subject', 'content','date_posted', 'photo', 'posted_by')
    search_fields = ('subject', 'date_posted')

    def save_model(self, request, obj, form, change):
        if not change:  # Only set on object creation
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)
