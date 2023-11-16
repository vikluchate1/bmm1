import users.models
from .models import InfoCard
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import pyotp
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import UserIP
from users.views import get_client_ip


def index(request):
    context = {
        'cards': InfoCard.objects.all()
    }
    try:
        if request.user and UserIP.objects.get(username=request.user.username):
            if not (get_client_ip(request) == UserIP.objects.get(username=request.user.username).ip_address):
                logout(request)
                return HttpResponseRedirect(reverse("users:login"))
    except users.models.UserIP.DoesNotExist:
        pass
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



