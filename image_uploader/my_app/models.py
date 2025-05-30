from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Image(models.Model):
    photo  = models.ImageField(_(""), upload_to="myimage", height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField( auto_now_add=True) 
    



