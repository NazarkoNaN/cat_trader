from django.db import models
from django.contrib.auth.models import User

class Cat(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=255, default='Kowbasuha')
