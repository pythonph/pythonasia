from django.db import models


class Sponsor(models.Model):
    class SponsorType(models.TextChoices):
        KEYSTONE = "KEYSTONE"
        PLATINUM = "PLATINUM"
        TITANIUM = "TITANIUM"
        GOLD = "GOLD"
        SILVER = "SILVER"

    name = models.CharField(max_length=255)
    logo_url = models.URLField(max_length=255)
    website_url = models.URLField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    sponsorship_date = models.DateField(blank=True, null=True)
    sponsor_type = models.CharField(max_length=255, choices=SponsorType.choices)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
