from django.db import models

class ShortenUrl(models.Model):
    url = models.CharField(max_length=255)
    shortCode = models.CharField(max_length=255,unique=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)
