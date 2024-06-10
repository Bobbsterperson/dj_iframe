from django.http import HttpResponse
from django.core.mail import send_mail

def simple_mail(request):
    try:
        send_mail(subject="piss", 
                  message='the message', 
                  from_email='mailtrap@demomailtrap.com', 
                  recipient_list=['bugstonn@gmail.com'],
                 
                  )
    except Exception as e:

        return HttpResponse(f"Hello, world. You're at the my_project index.{e}")
    return HttpResponse(f"yes")
