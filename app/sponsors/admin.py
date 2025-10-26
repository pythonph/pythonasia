from django.contrib import admin

from app.sponsors.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["name", "sponsor_type", "contact_name", "contact_email", "sponsorship_date", "created_at"]
    list_filter = ["sponsor_type", "sponsorship_date", "created_at"]
    search_fields = ["name", "contact_name", "contact_email", "info"]
    list_editable = ["sponsor_type"]
    ordering = ["sponsor_type", "name"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {"fields": ("name", "sponsor_type", "info")}),
        ("Media & Links", {"fields": ("logo_url", "website_url")}),
        ("Contact Information", {"fields": ("contact_name", "contact_email")}),
        ("Dates", {"fields": ("sponsorship_date", "created_at", "updated_at")}),
    )
