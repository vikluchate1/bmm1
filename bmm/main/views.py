
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
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        send_mail(
            #subject
            "testing",
            #message
            content,
            #from email
            settings.EMAIL_HOST_USER,
            #recipent list
            [to]
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




