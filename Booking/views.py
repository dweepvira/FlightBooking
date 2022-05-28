from multiprocessing import context
import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# from .models import BookForm
import Booking
from Booking.models import Book
from Booking.forms import BookForm
from Booking.models import Contact,Subscribe
# Create your views here.
@csrf_exempt
def home_view(request):
    if request.method == 'POST':
        if request.POST.get('email_id') and request.POST.get('con_number'):
            sub=Subscribe()
            sub.email_id= request.POST.get('email_id')
            sub.con_number= request.POST.get('con_number')
            sub.save()
            subs={
                'sub':sub
            }
            return render(request, 'index.html',subs)

    else:
        sub=Subscribe()
    return render(request,'index.html',)

def booking_view(request):
    # new_ticket_type = request.POST.get('ticket_type')
    # context={}
    # booking=BookForm.objects.all()
    # booking=BookForm(request.GET)
    if request.method == 'POST':
        if request.POST.get('r') and request.POST.get('ticket_from') and request.POST.get('ticket_to') and request.POST.get('depart') and request.POST.get('Return') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('travel_class'):
            post=Book()
            post.ticket_type= request.POST.get('r')
            post.ticket_from= request.POST.get('ticket_from')
            post.ticket_to= request.POST.get('ticket_to')
            post.depart= request.POST.get('depart')
            post.Return= request.POST.get('Return')
            post.adults= request.POST.get('adults')
            post.children= request.POST.get('children')
            post.travel_class= request.POST.get('travel_class')
            post.save()
            context={
                'post':post
            }
            return render(request,'book.html',context)
    
    else:
        post=Book()
    #     booking=BookForm(request.POST)
    #     if booking.is_valid():
    #         booking.save()
    #     else:
    #         booking=BookForm()
    return render(request, 'book.html',)


def contact_view(request):
    if request.method == 'POST':
        if request.POST.get('full_name') and request.POST.get('email') and request.POST.get('desc'):
            con=Contact()
            con.full_name= request.POST.get('full_name')
            con.email= request.POST.get('email')
            con.desc= request.POST.get('desc')
            con.save()
            cont={
                'con':con
            }
            return render(request, 'contact.html',cont)

    else:
        con=Contact()
    return render(request, 'contact.html',)


def Subs_view(request):
    if request.method == 'POST':
    
        return render(request, 'subs.html',)