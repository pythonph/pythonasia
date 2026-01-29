from django.contrib import admin

from app.sponsors.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "sponsor_type",
        "is_pao_connected",
        "contact_name",
        "contact_email",
        "sponsorship_date",
        "created_at",
    ]
    list_filter = ["sponsor_type", "is_pao_connected", "sponsorship_date", "created_at"]
    search_fields = ["name", "contact_name", "contact_email", "info"]
    list_editable = ["sponsor_type", "is_pao_connected"]
    ordering = ["sponsor_type", "name"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Basic Information", {"fields": ("name", "sponsor_type", "platinum_category", "is_pao_connected", "info")}),
        ("Media & Links", {"fields": ("logo_url", "website_url")}),
        ("Contact Information", {"fields": ("contact_name", "contact_email")}),
        ("Dates", {"fields": ("sponsorship_date", "created_at", "updated_at")}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.sponsor_type != Sponsor.SponsorType.PLATINUM:
            # Remove platinum_category from Basic Information if sponsor is not PLATINUM
            new_fieldsets = []
            for name, fieldset_dict in fieldsets:
                if name == "Basic Information":
                    fields = tuple(f for f in fieldset_dict["fields"] if f != "platinum_category")
                    new_fieldsets.append((name, {**fieldset_dict, "fields": fields}))
                else:
                    new_fieldsets.append((name, fieldset_dict))
            return tuple(new_fieldsets)
        return fieldsets
