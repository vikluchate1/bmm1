from django.db import models

class InfoCard(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='cards-images', blank=True)
    def __str__ (self):
        return f'[{self.pk}] {self.title}'
    


