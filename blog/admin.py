from django.contrib import admin
from django.db import models

from .models import Author, Post, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email_address')
    list_display_links = ('id','first_name')


admin.site.register(Author,AuthorAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','caption')
    list_display_links = ('id', 'caption')

admin.site.register(Tag, TagAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','posted_date')
    list_display_links = ('id', 'title')

admin.site.register(Post,PostAdmin)