from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Properties,Property_Availability,Property_Status,Reservation,Transaction

class PropertyAdmin(admin.ModelAdmin):
    model = Properties
    list_display = ['Property_Name']

class PropertyAvailabilityAdmin(admin.ModelAdmin):
    model = Property_Availability
    list_display = ['Property_Name','Available','Availability_StartTime','Availability_EndTime']


class PropertyStatusAdmin(admin.ModelAdmin):
    model = Property_Status
    list_display = ['Property_Name','Property_Status_Description','Expenses','Maintenance_ID']


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['Property_Name','Customer_Name','Date_From','Date_To']


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['Property_Name','Customer_Name','Trans_Amount']



admin.site.register(Properties,PropertyAdmin)
admin.site.register(Property_Availability,PropertyAvailabilityAdmin)
admin.site.register(Property_Status,PropertyStatusAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Transaction,TransactionAdmin)

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
