
from .models import InfoCard
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

import pyotp

def index(request):
    context = {
        'cards': InfoCard.objects.all()
    }
    return render(request,"main/project.html", context)

def sendemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        subject = request.POST.get('fromemail')
        to1 = request.POST.get("fromemail")
        content1 = "Здравствуйте, Ваша заявка находится в обработке, в скором времени с Вами свяжутся"
        subject1 = "Заявка на сайте BMMSUPPORT"
        send_mail(
            #subject
            subject,
            #message
            content,
            #from email
            settings.EMAIL_HOST_USER,
            #recipent list
            [to]
        )
        send_mail(
            #subject
            subject1,
            #message
            content1,
            #from email
            settings.EMAIL_HOST_USER,
            #recipent list
            [to1]
        )

        return render(
        request,
        'users/sendemail.html',
        {
        'title':'send an email'
        }
    )
    else:
        return render(
        request,
        'users/sendemail.html',
        {
        'title':'send an email'
        }
    )



