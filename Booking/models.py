from asyncio.windows_events import NULL
from dataclasses import fields
from tkinter.tix import Form
from django.db import models
from django import forms

# Create your models here.
# type_choices=(
#     ('one-way','ONE-WAY'),
#     ('return','RETURN'),
#     ('multi-city','MULTI-CITY'),
# )
# travel_choices=(
#     ('first-class/1A','First-Class/1A'),
#     ('ac2tier/2A','Ac2Tier/2A'),
#     ('ac3tier/3A','Ac3Tier/3A'),
#     ('ec class/economyclass','Ec Class/Economy CLass'),
#     ('ac chair car','Ac Chair Car'),
#     ('sleeper class','Sleeper Class'),
#     ('second class','Second Class'),
#     ('general','General'),
# )
# class Book(forms.Form):
#     ticket_type =forms.ChoiceField(widget=forms.RadioSelect,choices=type_choices)
#     ticket_from =forms.CharField(max_length=100)
#     ticket_to =forms.CharField(max_length=100)
#     depart =forms.DateField()
#     Return =forms.DateField()
#     adults =forms.IntegerField()
#     children =forms.IntegerField()
#     travel_class=forms.ChoiceField(choices=travel_choices)
    # choices=type_choices
class Book(models.Model):
    ticket_type =models.CharField(max_length=50)
    ticket_from =models.CharField(max_length=100)
    ticket_to =models.CharField(max_length=100)
    depart =models.DateField()
    Return =models.DateField()
    adults =models.IntegerField()
    children =models.IntegerField(null=True)
    travel_class=models.CharField(max_length=100)

class Contact(models.Model):
    full_name =models.CharField(max_length=150)
    email =models.EmailField()
    desc =models.CharField(max_length=300)

class Subscribe(models.Model):
    email_id =models.EmailField()
    con_number =models.CharField(max_length=10)
    
# class CustomForm(forms.ModelForm):     
#     class Meta: 
#         model = Book
#         fields='__all__'
#         widgets = {'ticket_type': forms.RadioSelect}
    # ticket_type=forms.ChoiceField(choices=type_choices,widgets=forms.RadioSelect)
    

