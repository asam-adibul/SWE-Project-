from .models import Listing


def pending_listings(request):
    if request.user.is_authenticated and request.user.is_superuser:
        count = Listing.objects.filter(approved=False).count()
        return {'pending_listings_count': count}
    return {'pending_listings_count': 0}