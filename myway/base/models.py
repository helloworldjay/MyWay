from django.db import models

# Create your models here.
class User_info(models.Model):
    photo = models.ImageField(blank=True) # photo for medical check
    is_fhp = models.BooleanField(default=False) # is fhp or not
    