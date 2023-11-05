from django.urls import path
from .views import auth,UserLoginView,logout_view,send_email

app_name = 'users'
urlpatterns = [
    path('auth/', auth, name = 'auth'),
    # path('login/', login, name = 'login'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('sendemail/', send_email, name='sendemail')
]