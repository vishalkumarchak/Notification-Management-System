import requests
from decouple import config

from notifications.models import WebPushSubscription


class WebPushService:

    @staticmethod
    def send(user, title, message):

        subscriptions = WebPushSubscription.objects.filter(
            user=user
        )

        if not subscriptions.exists():
            return None

        subscription_ids = list(
            subscriptions.values_list(
                'subscription_id',
                flat=True
            )
        )

        url = "https://api.onesignal.com/notifications"

        headers = {
            "Authorization": f"Key {config('ONESIGNAL_REST_API_KEY')}",
            "Content-Type": "application/json",
        }

        payload = {
            "app_id": config('ONESIGNAL_APP_ID'),
            "include_subscription_ids": subscription_ids,
            "headings": {
                "en": title
            },
            "contents": {
                "en": message
            },
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        return response