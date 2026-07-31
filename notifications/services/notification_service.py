from django.template import Template, Context
from .whatsapp_service import WhatsAppService
from .email_service import EmailService
from .webpush_service import WebPushService

from notifications.models import (
    Trigger,
    NotificationTemplate,
    NotificationLog
)

def render_text(text, variables):

    template = Template(text)

    context = Context(variables)

    return template.render(context)


class NotificationService:

    @staticmethod
    def fire(trigger_code, user, variables=None):

        variables = variables or {}

        try:
            trigger = Trigger.objects.get(
                code=trigger_code
            )
        except Trigger.DoesNotExist:
            return

        templates = NotificationTemplate.objects.filter(
            trigger=trigger,
            is_enabled=True
        )

        for template in templates:

            body = render_text(
                template.body,
                variables
            )

            subject = render_text(
                template.subject or '',
                variables
            )

            title = render_text(
                template.title or '',
                variables
            )

            try:

                if template.channel == 'whatsapp':

                    response = WhatsAppService.send(
                        user.profile.phone_number,
                        body
                    )

                elif template.channel == 'email':

                    response = EmailService.send(
                        user.email,
                        subject,
                        body
                    )

                elif template.channel == 'webpush':

                    response = WebPushService.send(
                        user,
                        title,
                        body
                    )

                NotificationLog.objects.create(
                    user=user,
                    trigger=trigger,
                    channel=template.channel,
                    status='success',
                    response=str(response.text if response else '')
                )

            except Exception as e:

                NotificationLog.objects.create(
                    user=user,
                    trigger=trigger,
                    channel=template.channel,
                    status='failed',
                    response=str(e)
                )