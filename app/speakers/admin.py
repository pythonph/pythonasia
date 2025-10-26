from django.contrib import admin

from app.speakers.models import Speaker, SpeakerPresentation, SpeakerSchedule, SpeakerSocial


class SpeakerSocialInline(admin.TabularInline):
    model = SpeakerSocial
    extra = 1
    fields = ("platform", "username", "url")


class SpeakerPresentationInline(admin.TabularInline):
    model = SpeakerPresentation
    extra = 1
    fields = ("title", "presentation_type", "description", "abstract")


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "is_featured", "created_at")
    list_filter = ("is_featured", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "email", "title")
    list_editable = ("is_featured",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Personal Information", {"fields": ("first_name", "last_name", "middle_name", "title")}),
        ("Contact & Media", {"fields": ("email", "photo_url")}),
        ("Content", {"fields": ("introduction", "bio")}),
        ("Settings", {"fields": ("is_featured",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    inlines = [SpeakerSocialInline, SpeakerPresentationInline]


@admin.register(SpeakerSocial)
class SpeakerSocialAdmin(admin.ModelAdmin):
    list_display = ("speaker", "platform", "username", "url")
    list_filter = ("platform", "created_at")
    search_fields = ("speaker__first_name", "speaker__last_name", "platform", "username")
    readonly_fields = ("created_at", "updated_at")


@admin.register(SpeakerPresentation)
class SpeakerPresentationAdmin(admin.ModelAdmin):
    list_display = ("title", "speaker", "presentation_type", "created_at")
    list_filter = ("presentation_type", "created_at", "updated_at")
    search_fields = ("title", "speaker__first_name", "speaker__last_name", "description")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Presentation Details", {"fields": ("title", "speaker", "presentation_type")}),
        ("Content", {"fields": ("description", "abstract")}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


@admin.register(SpeakerSchedule)
class SpeakerScheduleAdmin(admin.ModelAdmin):
    list_display = ("presentation", "speaker", "day", "track", "time_start", "time_end", "location")
    list_filter = ("day", "track", "time_start", "created_at")
    search_fields = ("presentation__title", "speaker__first_name", "speaker__last_name", "location")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Schedule Details", {"fields": ("presentation", "speaker", "day", "track")}),
        ("Timing & Location", {"fields": ("time_start", "time_end", "location")}),
        ("Additional Information", {"fields": ("description",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
