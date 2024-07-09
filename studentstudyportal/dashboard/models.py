from django.db import models
from django.contrib.auth.models import User

class notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
       return self.title 
    class Meta:
     verbose_name="notes"
     verbose_name_plural="notes"
class hw(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   subject=models.CharField(max_length=200)
   title=models.CharField(max_length=200)
   description=models.CharField(max_length=200)
   due=models.CharField(max_length=200)
   def __str__(self):
       return self.title 
   class Meta:
     verbose_name="hw"
     verbose_name_plural="hw"
class td(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   title=models.CharField(max_length=100)   
   status=models.BooleanField(default=False)  
