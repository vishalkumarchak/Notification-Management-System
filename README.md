# Notification System (Django + Tailwind CSS)

A centralized notification management system built with **Django, Django Templates, Tailwind CSS, PostgreSQL, WhatsApp Cloud API, Postmark, and OneSignal Web Push**.

The goal of this project is to allow administrators to manage **all notification templates from a single dashboard** without logging into WhatsApp, Postmark, or OneSignal separately.

---

## Features

* Centralized notification dashboard
* Trigger-based notifications
* WhatsApp integration (Meta Cloud API Sandbox)
* Email integration (Postmark)
* Browser Web Push notifications (OneSignal)
* Enable/disable notification channels
* Test notification sending
* Notification logs
* User activity tracking
* Inactive user notifications (1 day / 7 days)

---

## Tech Stack

| Layer      | Technology         |
| ---------- | ------------------ |
| Backend    | Django             |
| Frontend   | Django Templates   |
| Styling    | Tailwind CSS       |
| Database   | PostgreSQL / MySQL |
| Email      | Postmark           |
| WhatsApp   | Meta Cloud API     |
| Web Push   | OneSignal          |
| Scheduler  | Celery + Redis     |
| Deployment | Render             |

---

## Project Structure

notification-system/

accounts/

notifications/

config/

templates/

static/

media/

manage.py

requirements.txt

README.md

---

## Triggers

The system supports trigger-based notifications.

Current implemented triggers:

* Login
* Logout
* Not logged in for 1 day
* Not logged in for 7 days

Each trigger can send notifications on:

* WhatsApp
* Email
* Web Push

---

## Notification Dashboard

The admin panel contains a single table.

| Trigger              | WhatsApp | Email | Web Push |
| -------------------- | -------- | ----- | -------- |
| Login                | Edit     | Edit  | Edit     |
| Logout               | Edit     | Edit  | Edit     |
| Not logged in 1 day  | Edit     | Edit  | Edit     |
| Not logged in 1 week | Edit     | Edit  | Edit     |

Each cell allows:

* Create template
* Edit template
* Enable / Disable
* Test Send

---

## Installation

### Clone repository

git clone https://github.com/your-username/notification-system.git

cd notification-system

### Create virtual environment

python -m venv venv

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

### Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a **.env** file.

SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=notification_db

DB_USER=root

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=3306

WHATSAPP_ACCESS_TOKEN=your_token

PHONE_NUMBER_ID=your_phone_number_id

POSTMARKAPP_TOKEN=your_postmark_token

POSTMARK_FROM_EMAIL=[verified_email@example.com](mailto:verified_email@example.com)

ONESIGNAL_APP_ID=your_app_id

ONESIGNAL_REST_API_KEY=your_rest_api_key

---

## Database Setup

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

---

## Run Development Server

python manage.py runserver

Visit:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

---

## Initial Triggers

Create initial triggers.

python manage.py shell

from notifications.models import Trigger

Trigger.objects.get_or_create(code='login', name='Login')

Trigger.objects.get_or_create(code='logout', name='Logout')

Trigger.objects.get_or_create(code='inactive_1_day', name='Not logged in for 1 day')

Trigger.objects.get_or_create(code='inactive_1_week', name='Not logged in for 1 week')

---

## Web Push Setup

1. Create a OneSignal account.
2. Create a Web Push app.
3. Add the OneSignal App ID.
4. Allow browser notifications.
5. The subscription ID will automatically be stored in the database.

---

## WhatsApp Setup

1. Create a Meta Developer account.
2. Create a WhatsApp Cloud API app.
3. Use the sandbox test number.
4. Add your phone number to the test recipients.
5. Add the token to **.env**.

---

## Postmark Setup

1. Create a Postmark account.
2. Create a developer server.
3. Verify your sender email.
4. Add the server token to **.env**.

---

## Celery

Start Redis.

Start Celery worker.

celery -A config worker -l info

Start Celery Beat.

celery -A config beat -l info

The inactivity check runs daily.

---

## Testing

### Login Trigger

* Login to the website.
* NotificationService fires the **login** trigger.
* WhatsApp / Email / Web Push are sent if enabled.

### Logout Trigger

* Logout from the website.
* NotificationService fires the **logout** trigger.

### Inactive User Trigger

* User remains inactive.
* Celery task checks last activity.
* Sends 1-day or 7-day reminder notifications.

---

## Deployment (Render)

Build command:

./build.sh

Start command:

gunicorn config.wsgi:application

Required environment variables:

* SECRET_KEY
* DEBUG=False
* DATABASE_URL
* WHATSAPP_ACCESS_TOKEN
* PHONE_NUMBER_ID
* POSTMARKAPP_TOKEN
* POSTMARK_FROM_EMAIL
* ONESIGNAL_APP_ID
* ONESIGNAL_REST_API_KEY

---

## Author

**Vishal Kumar Chak**

Python Django Full Stack Developer

This project was built as a centralized multi-channel notification management system using Django and Tailwind CSS.
"# Notification-Management-System" 
