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
        return f"{self.title} "




#The bellow model for comment will be a one to many rlationship 

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=450)
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="comments") #on_delet Cascade will delete the comment if the poste will be deleted