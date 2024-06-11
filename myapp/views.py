from django.shortcuts import render
from django.http import HttpResponse
from myapp.utils import send_custom_email

def send_email_view(request):

    context = {
        'user_name': 'John Doe',
        'custom_message': 'eat shit and die',
        'subject': 'Your Custom Subject'
    }
    send_custom_email('Your Custom Subject', 'bugstonn@gmail.com', context)
    return HttpResponse("Email sent")