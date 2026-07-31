from django.contrib import admin

from .models import (
    Trigger,
    NotificationTemplate,
    WebPushSubscription,
    NotificationLog
)


@admin.register(Trigger)
class TriggerAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
        'created_at'
    )


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):

    list_display = (
        'trigger',
        'channel',
        'is_enabled'
    )

    list_filter = (
        'channel',
        'is_enabled'
    )


@admin.register(WebPushSubscription)
class WebPushSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_id')


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'trigger',
        'channel',
        'status',
        'created_at'
    )

    list_filter = (
        'channel',
        'status'
    )