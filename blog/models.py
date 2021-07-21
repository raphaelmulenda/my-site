from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=False)
    image_name = models.ImageField()
