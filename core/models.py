from django.contrib.auth.models import User
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, default='default value')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
 