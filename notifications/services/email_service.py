import requests
from decouple import config

class EmailService:

    @staticmethod
    def send(to_email, subject, body):

        url = "https://api.postmarkapp.com/email"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Postmark-Server-Token": config('POSTMARKAPP_TOKEN'),
        }

        payload = {
            "From": config('POSTMARK_FROM_EMAIL'),
            "To": to_email,
            "Subject": subject,
            "TextBody": body,
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        return response