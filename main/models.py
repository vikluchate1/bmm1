from django.db import models
from django.utils import timezone
class InfoCard(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='cards-images', blank=True)
    def __str__ (self):
        return f'[{self.pk}] {self.title}'
    

class MailLogs(models.Model):
    content = models.TextField()
    email_address = models.EmailField()
    date = models.DateTimeField(default=timezone.now())
    def __str__ (self):
        return f'[{self.pk}] {self.email_address}'