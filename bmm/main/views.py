from django.shortcuts import render
from .models import InfoCard
def index(request):
    context = {
        'cards': InfoCard.objects.all()
    }
    return render(request,"main/project.html", context)


