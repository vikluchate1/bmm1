
from django.urls import path
# from . import views
from .views import index, pusher_auth, generate_agora_token,call_user
app_name = 'agora'
urlpatterns = [
    path(' ', index, name='agora-index'),
    path('pusher/auth/', pusher_auth, name='agora-pusher-auth'),
    path('token/',generate_agora_token, name='agora-token'),
    path('call-user/', call_user, name='agora-call-user'),
]
