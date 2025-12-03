from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount", "name","email", "date", "message")
    search_fields = ("name", "date", "email")
