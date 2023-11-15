from django.urls import path

from bmm.users.views import send_email

app_name = "main"
urlpatterns = [
 path('sendemail/', send_email, name='sendemail'),


 ]