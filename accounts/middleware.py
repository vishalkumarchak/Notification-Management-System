from django.utils import timezone
from accounts.models import UserProfile

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile, created = UserProfile.objects.get_or_create(
                user=request.user,
                defaults={'phone_number': '919999999999'}
            )
            profile.last_activity = timezone.now()
            profile.save(update_fields=['last_activity'])

        response = self.get_response(request)
        return response