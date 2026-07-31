from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ( Trigger, NotificationTemplate)
from .services.notification_service import NotificationService
import json
from django.http import JsonResponse
from .models import WebPushSubscription

@login_required
def dashboard(request):
    triggers = Trigger.objects.all()

    channels = [
        'whatsapp',
        'email',
        'webpush'
    ]

    return render(request, 'notifications/dashboard.html',
        {
            'triggers': triggers,
            'channels': channels
        }
    )


@login_required
def edit_template(request, trigger_id, channel):

    trigger = get_object_or_404(Trigger, id=trigger_id)

    template, _ = NotificationTemplate.objects.get_or_create(trigger=trigger,channel=channel)

    if request.method == 'POST':
        template.subject = request.POST.get('subject', '')
        template.title = request.POST.get('title', '')
        template.body = request.POST.get('body', '')
        template.is_enabled = 'enabled' in request.POST

        template.save()

        messages.success( request,'Template updated successfully')

        return redirect('dashboard')

    return render(
        request,
        'notifications/template_form.html',
        {
            'trigger': trigger,
            'template': template,
            'channel': channel
        }
    )


@login_required
def webpush_subscribe(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        subscription_id = data.get('subscription_id')

        WebPushSubscription.objects.update_or_create( user=request.user,
            defaults={
                'subscription_id': subscription_id
            }
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


@login_required
def toggle_template(request, template_id):

    template = get_object_or_404(NotificationTemplate, id=template_id)
    template.is_enabled = not template.is_enabled
    template.save(update_fields=['is_enabled'])

    return JsonResponse({'enabled': template.is_enabled})


@login_required
def test_send(request, template_id):

    template = get_object_or_404(NotificationTemplate, id=template_id)

    NotificationService.fire(template.trigger.code, request.user,
        {
            'name': request.user.first_name or request.user.username
        }
    )

    messages.success(request,'Test notification sent')

    return redirect('dashboard')