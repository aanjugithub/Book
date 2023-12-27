from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    author=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    #for adding pic frsrt come to models.py and add required data here picture is gona add

    pictures=models.ImageField(upload_to="images",null=True) #null needs to set otherwise it wll effect other feilds.after this run migration commnds 2nos
    
   

    def __str__(self):
        return self.name