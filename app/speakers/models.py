from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    photo_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"


class SpeakerSocial(models.Model):
    speaker = models.ForeignKey("speaker", on_delete=models.CASCADE, related_name="socials")
    platform = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["platform"]
        verbose_name = "Speaker Social"
        verbose_name_plural = "Speaker Socials"


class SpeakerPresentation(models.Model):
    class PresentationTypes(models.TextChoices):
        TALK = "talk"
        WORKSHOP = "workshop"
        PANEL = "panel"

    speaker = models.ForeignKey(
        "speaker",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="presentations",
    )
    title = models.CharField(max_length=255)
    presentation_type = models.CharField(max_length=255, choices=PresentationTypes.choices)
    description = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Speaker Presentation"
        verbose_name_plural = "Speaker Presentations"


class SpeakerSchedule(models.Model):
    class Days(models.TextChoices):
        DAY_1 = "day_1"
        DAY_2 = "day_2"

    class Tracks(models.TextChoices):
        TRACK_1 = "track_1"
        TRACK_2 = "track_2"
        TRACK_3 = "track_3"

    speaker = models.ForeignKey(
        "speaker",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="schedules",
    )
    presentation = models.ForeignKey(
        "speakerpresentation",
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    day = models.CharField(max_length=255, choices=Days.choices)
    track = models.CharField(max_length=255, choices=Tracks.choices)
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_time(self):
        fmt = "%-I:%M %p"
        return f"{self.time_start.strftime(fmt)} - {self.time_end.strftime(fmt)}"

    @property
    def display_start_time(self):
        return self.time_start.strftime("%H:%M:%S")

    @property
    def display_end_time(self):
        return self.time_end.strftime("%H:%M:%S")

    class Meta:
        verbose_name = "Speaker Schedule"
        verbose_name_plural = "Speaker Schedules"
