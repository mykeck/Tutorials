from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    tutorial_image = CloudinaryField('image')
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
        
