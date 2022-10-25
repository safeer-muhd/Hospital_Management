from django.contrib import admin
from . models import Booking, Departments
from . models import Doctors

# Admin page Booking Model class

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booked_on','booking_date')




# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)