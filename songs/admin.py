from django.contrib import admin
from . import models



# Register your models here.
@admin.register(models.Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'lyrics')
    search_fields = ('title', 'artist')