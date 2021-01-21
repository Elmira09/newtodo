from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
<<<<<<< HEAD
    created_a t= models.DateField(auto_now_add=True)
=======
    created_at= models.DateField(auto_now_add=True)
>>>>>>> 24c20807dd32015c796906cad8d65d2ace66cc4a
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default = False)
