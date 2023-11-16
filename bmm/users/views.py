from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import UserIP



def auth(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            ip = UserIP(username=request.POST['username'], ip_address=get_client_ip(request))
            ip.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, "users/auth.html", context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_email(request):
    return render(request, "users/sendemail.html")

def policy(request):
    return render(request, "users/policy.html")
# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, "users/login.html", context)

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    redirect_authenticated_user = reverse_lazy('index')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))





