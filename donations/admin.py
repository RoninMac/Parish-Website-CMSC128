from django.contrib import admin
from .models import DonationInfo

@admin.register(DonationInfo)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount", "name","email","message", "date")
    search_fields = ("name", "date", "email")
