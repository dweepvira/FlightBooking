
from django.db import models



class Book(models.Model):
    ticket_type =models.CharField(max_length=50)
    ticket_from =models.CharField(max_length=100)
    ticket_to =models.CharField(max_length=100)
    depart =models.DateField()
    Return =models.DateField()
    adults =models.IntegerField()
    children =models.IntegerField(null=True)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=13)
    emailid=models.EmailField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name =models.CharField(max_length=150)
    email =models.EmailField()
    desc =models.CharField(max_length=300)

class Subscribe(models.Model):
    email_id =models.EmailField()
    con_number =models.CharField(max_length=13)


class Plan(models.Model):
    dest=models.CharField(max_length=150)
    strdate=models.DateField()
    enddate=models.DateField()
    adults1=models.IntegerField()
    children1=models.IntegerField()
    f_name=models.CharField(max_length=150)
    ph_num=models.CharField(max_length=13)
    hot_cat=models.CharField(max_length=150)
    lnd_trns=models.CharField(max_length=150)
    transport=models.CharField(max_length=150)

    def __str__(self):
        return self.f_name
    
