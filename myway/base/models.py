from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User_info(models.Model):
    photo = models.ImageField(blank=True) # photo for medical check
    is_fhp = models.BooleanField(default=False) # is fhp or not
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
