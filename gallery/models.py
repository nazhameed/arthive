from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE, related_name='artworks')
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
