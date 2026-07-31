from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from notifications.services.notification_service import NotificationService

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            NotificationService.fire(
                'login',
                user,
                {
                    'name': user.first_name or user.username
                }
            )

            messages.success(
                request,
                'Login successful'
            )

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password'
        )

    return render(request, 'login.html')


def logout_view(request):

    if request.user.is_authenticated:

        NotificationService.fire(
            'logout',
            request.user,
            {
                'name': request.user.first_name or request.user.username
            }
        )

    logout(request)

    messages.success(
        request,
        'Logout successful'
    )

    return redirect('login')


def home(request):
    return render(request, 'home.html')


