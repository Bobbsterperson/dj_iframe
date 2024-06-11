from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_custom_email(subject, recipient_email, context):
    html_message = render_to_string('email_template.html', context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        'bugstonn@gmail.com',
        [recipient_email],
        html_message=html_message,
    )
