from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
