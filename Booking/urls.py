from django.urls import re_path
from . import views
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.conf.urls import url
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('',TemplateView.as_view(template_name='book.html'),name='book'),
    path('',TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]