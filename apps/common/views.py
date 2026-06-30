from django.http import JsonResponse


def health_check(request):
    """Return a lightweight service health response."""
    return JsonResponse({
        "status": "ok",
        "service": "nextoffer",
        "version": "v1",
    })
