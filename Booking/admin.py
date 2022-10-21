from django.contrib import admin

from Booking.models import Book
from Booking.models import Contact
# Register your models here.
from .models import Contact, Plan,Subscribe
  
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email_id', 'con_number')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True

admin.site.register(Book)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Subscribe,SubscribeAdmin)
admin.site.register(Plan)
# admin.site.register(BookForm)
# admin.site.register(CustomForm)