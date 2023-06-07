from django.db import models

# Create your models here.
class Bank(models.Model):
    BankName=models.CharField(max_length=20)
    Branch=models.CharField(max_length=40)
    IFSC=models.CharField(max_length=20)
    
    def __str__(self):
        return self.BankName
    
class Customer(models.Model):
    CName=models.CharField(max_length=20)
    CAcno=models.BigIntegerField()
    CAddr=models.CharField(max_length=200)
    Requirement=models.CharField(max_length=20)
    Bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.CName