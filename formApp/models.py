from django.db import models
from django.forms import IntegerField

# Create your models here.
class addStd(models.Model):
    stdId=models.IntegerField(primary_key=True)
    stdName=models.CharField(max_length=25)
    stdEmail=models.EmailField()
    stdPassword=models.CharField(max_length=25)

    def __str__(self):
        return str(self.stdName)
