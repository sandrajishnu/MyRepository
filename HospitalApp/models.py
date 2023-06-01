from django.db import models

# Create your models here.
class HospitalDB(models.Model):
    Hospital_Name = models.CharField(max_length=30, null=True, blank=True)
    District = models.CharField(max_length=30, null=True, blank=True)
    Location = models.CharField(max_length=30, null=True, blank=True)
    Contact_Number = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Images")


class DoctorsDB(models.Model):
    Hospital_Name = models.CharField(max_length=50, null=True, blank=True)
    Doctor_Name = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Contact_Number = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="DoctorsImages", null=True, blank=True)
