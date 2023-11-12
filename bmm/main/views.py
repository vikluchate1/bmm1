
from .models import InfoCard
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {
        'cards': InfoCard.objects.all()
    }
    return render(request,"main/project.html", context)

def sendemail(request):
    return render(
        request,
        'users/sendemail.html',
        {
        'title':'send an email'
        }
    )




