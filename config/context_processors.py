from django.conf import settings


def static_version(request):
    """
    Add STATIC_VERSION to template context for cache busting.
    """
    return {"STATIC_VERSION": settings.STATIC_VERSION}
