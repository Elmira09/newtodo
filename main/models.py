from django.db import models



class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle =  models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price =  models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.DateField(auto_now=True)
    published_at = models.DateField(auto_now_add=True)



   

