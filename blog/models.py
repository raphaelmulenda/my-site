from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self) :
        return f"{self.first_name}   {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self) :
        return f"{self.caption} "
 

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=False)
    image_name = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    posted_date = models.DateField(blank=False)
    slug = models.SlugField(default="",blank=True, unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) :
        return f"{self.title} {self.excerpt}"




