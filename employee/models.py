from django.db import models

# Create your models here.
class employee(models.Model):
    Name=models.CharField(max_length=255)
    Start_date=models.DateField()
    End_date=models.DateField()
    Reason=models.CharField(max_length=255)
    Status=models.IntegerField(default=0)