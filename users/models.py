from django.db import models


#Создание полей для таблицы в бд с ip
class UserIP(models.Model):
    username = models.CharField(max_length=150, unique=True)
    ip_address = models.GenericIPAddressField(unpack_ipv4=True)
