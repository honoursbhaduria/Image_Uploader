from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Image(models.Model):
    photo  = models.ImageField(upload_to="myimage")
    date = models.DateTimeField( auto_now_add=True) 
    


