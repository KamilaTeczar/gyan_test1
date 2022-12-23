from django.db import models

# Create your models here.
class properties(models.Model):
    name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    def __str__(self):
            return self.name
class properties_2(models.Model):
    Properties=models.ForeignKey(properties,on_delete=models.CASCADE)
    price=models.IntegerField()
    completion_date=models.CharField(max_length=100)
   
    def __str__(self):
            return self.name
