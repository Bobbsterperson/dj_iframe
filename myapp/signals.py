from django.conf import settings
from django.core.mail import send_mail
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    subject = 'Welcome to Our Website'
    message = f'Hi {user.username},\n\nThank you for registering at our website.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
