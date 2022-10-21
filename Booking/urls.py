from django.urls import re_path
from . import views
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.conf.urls import url
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='home',),
    path('',TemplateView.as_view(template_name='book.html'),name='book'),
    path('',TemplateView.as_view(template_name='contact.html'),name='contact'), 
    path('',TemplateView.as_view(template_name='login.html'),name='login'),
    path('',TemplateView.as_view(template_name='termsAndCon.html'),name='termsandcon'),
    path('',TemplateView.as_view(template_name='customer.html'),name='customer'),
    path('',TemplateView.as_view(template_name='about.html'),name='about'),
    path('',TemplateView.as_view(template_name='plans.html'),name='plans'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]