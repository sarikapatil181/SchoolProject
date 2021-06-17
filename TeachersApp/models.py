from django.db import models

# Create your models here.
class Teachers(models.Model):
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    profilepic=models.ImageField(upload_to='uploads/profilepic/')
    email=models.CharField(max_length=50,primary_key=True)
    phonenum=models.CharField(max_length=50,default="")
    roomnum=models.CharField(max_length=50,default="")
    subjects=models.CharField(max_length=300,default="")
    
    
    def __str__(self):
        return self.fname
