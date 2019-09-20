from django.db import models

# Create your models here.
class Contact(models.Model):
    senderName = models.TextField()
    senderEmail = models.EmailField()
    details = models.TextField()
