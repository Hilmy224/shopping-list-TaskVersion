from django.db import models

#Imports for making everyuser has diffrent data
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    species=models.CharField(max_length=255,default="Uknown")
    amount = models.IntegerField()
    spiritStatus=models.CharField(max_length=255,default="Uknown")
    causeOfDeath=models.CharField(max_length=255,default="Uknown")
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)   
    
   

    