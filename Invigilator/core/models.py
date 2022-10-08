from django.db import models

# Create your models here.

class Invigilator(models.Model):
    name=models.CharField(max_length=50)
    staff_id=models.CharField( max_length=10)
    address=models.CharField( max_length=50)
    joined=models.DateField( auto_now=False, auto_now_add=False)
    department=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)

    