from django.db import models

class Contact(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    subject = models.CharField('Subject', max_length=100)
    message = models.CharField('Message', max_length=5000)
