from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from notifications.services.notification_service import NotificationService

@shared_task
def check_inactive_users():

    now = timezone.now()
    users = User.objects.select_related('profile')
    for user in users:
        inactive_days = (now - user.profile.last_activity).days

        if inactive_days == 1:
            NotificationService.fire('inactive_1_day', user,
                {
                    'name': user.first_name or user.username
                }
            )

        elif inactive_days == 7:
            NotificationService.fire('inactive_1_week', user,
                {
                    'name': user.first_name or user.username
                }
            )
