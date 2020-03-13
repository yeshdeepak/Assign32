from django.db import models

# Create your models here.

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Street_Address = models.CharField(max_length=50, default=' ', null=True, blank=True)
    City = models.CharField(max_length=50, default=' ', null=True, blank=True)
    State = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Zip = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
    User_Role = models.CharField(max_length=50, default=' ', null=True, blank=True)
