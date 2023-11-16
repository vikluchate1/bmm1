from django.contrib import admin
from .models import InfoCard, MailLogs
# @admin.register(InfoCard)
# class InfoCardAdmin (admin.ModelAdmin):

admin.site.register(InfoCard)
admin.site.register(MailLogs)
