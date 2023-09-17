from django.db import models

# Create your models here.date_added = models.DateField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    species=models.CharField(max_length=255,default="Uknown")
    amount = models.IntegerField()
    spiritStatus=models.CharField(max_length=255,default="Uknown")
    causeOfDeath=models.CharField(max_length=255,default="Uknown")
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
   

    