from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('template/<int:template_id>/toggle/', views.toggle_template, name='toggle_template'),
    path('webpush/subscribe/', views.webpush_subscribe, name='webpush_subscribe'),
    path('test/<int:template_id>/', views.test_send, name='test_send'),
    path('template/<int:trigger_id>/<str:channel>/', views.edit_template, name='edit_template'),
]
