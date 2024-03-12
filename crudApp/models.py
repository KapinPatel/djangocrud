from django.db import models

# Create your models here.
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    ceo=models.CharField(max_length=50)
    about=models.TextField()
    
    def __str__ (self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    address=models.CharField(max_length=200)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
