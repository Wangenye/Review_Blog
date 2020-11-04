from django.db.models import fields
from .models import Comment,Newsletter,Contactus
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields =('email',)
# def should_be_empty(value):
#     if value:
#         return forms.ValidationError("Field Is not empty")
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields =('email','name','message')