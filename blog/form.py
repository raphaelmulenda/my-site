from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        exclude = ["post"] # this code will take evrything else from Comment model excpet the Post , an other way to do this is to create a list with all needed fields
        labels = {"user_name": "Your Name",
                  "user_email": "Your Email",
                  "text": "Your Comment"}
        
        
