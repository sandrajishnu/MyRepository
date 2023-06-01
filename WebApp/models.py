from django.db import models

# Create your models here.

class AppointmentDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    D_Name = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    ContactN = models.IntegerField( null=True, blank=True)
    Message = models.CharField(max_length=300, null=True, blank=True)


class LogindataDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.EmailField(max_length=50, null=True, blank=True)
