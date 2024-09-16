from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()

    def __str__(self):
        return self.phone
