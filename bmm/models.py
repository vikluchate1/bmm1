from django.db import models


class Profile(models.Model):
    login = models.CharField(max_length=30,unique=True)
    channel_name = models.CharField(max_length=250,unique=True)

