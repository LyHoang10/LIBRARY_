from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class CustomerExtraForm(forms.ModelForm):
    class Meta:
        model=models.CustomerExtra
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['title','authors','genres']

class BorrowedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    enrollment2=forms.ModelChoiceField(queryset=models.CustomerExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')
    
