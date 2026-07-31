import requests
from decouple import config


class WhatsAppService:

    @staticmethod
    def send(phone_number, message):

        token = config('WHATSAPP_ACCESS_TOKEN')
        phone_id = config('PHONE_NUMBER_ID')

        url = f"https://graph.facebook.com/v23.0/{phone_id}/messages"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        return response