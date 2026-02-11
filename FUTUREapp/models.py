# Create your models here.
from django.db import models

class Places(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title