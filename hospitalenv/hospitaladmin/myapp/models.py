from django.db import models

# Create your models here.


class appointment(models.Model):
    patientname=models.CharField(max_length=150)
    appointmentdate=models.CharField(max_length=150)
    symptoms=models.CharField(max_length=200)
    departmentname=models.CharField(max_length=50)
    doctorname=models.CharField(max_length=100)
    def __str__(self) :
        return self.patientname
    

class doctorregdb(models.Model):
    doctorname=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100)
    specialisation=models.CharField(max_length=200)
    dob=models.CharField(max_length=200)
    address=models.CharField(max_length=250)
    contact=models.CharField(max_length=200)
    wdays=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.doctorname
    
class Patientdb(models.Model):
    patientname=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    dob=models.DateField(max_length=200)
    mobile=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.patientname
    

class contact(models.Model):
    patientname=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    email=models.CharField(max_length=150)
    message=models.CharField(max_length=200)
    def __str__(self):
        return self.patientname
    
class Department(models.Model):
    departmentno = models.CharField(max_length=200)
    departmentname = models.CharField(max_length=200)
    departmenthead = models.CharField(max_length=200)
    def __str__(self):
        return self.departmenthead
    