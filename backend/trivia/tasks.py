from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_email):
    subject = "Регистрация прошла успешно"
    message = "Спасибо за регистрацию на нашем сайте!"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
