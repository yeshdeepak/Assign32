from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Properties(models.Model):
    Property_Name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    Property_Description = models.CharField(max_length=50,blank=False, null=False, default=' ')
    Property_Guest_Capacity = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Property_Street = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Property_City = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Property_State = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Price = models.CharField(max_length=50, blank=True, null=True,default=' ')
    No_of_Rooms = models.CharField(max_length=50, blank=True, null=True,default=' ')
    No_of_Bathrooms = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Total_Area = models.CharField(max_length=50, blank=True, null=True,default=' ')
    Garage_Size = models.CharField(max_length=50, blank=True, null=True,default=' ')
    No_of_Floors = models.CharField(max_length=50, blank=True, null=True,default=' ')

    def __str__(self):
        return self.Property_Name


# Create your models here.
class Property_Availability(models.Model):
    Property_Name = models.ForeignKey(Properties,on_delete=models.CASCADE)
    Available = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Availability_StartTime=models.DateTimeField(blank=True, null=True)
    Availability_EndTime=models.DateTimeField(blank=True, null=True)

class Property_Status(models.Model):
    Property_Name = models.ForeignKey(Properties,on_delete=models.CASCADE)
    Report_TimeDate = models.DateTimeField(blank=True, null=True)
    Property_Status_Description=models.CharField(max_length=50,blank=True, null=True)
    Expenses=models.CharField(max_length=50, default=' ', null=True, blank=True)
    Comments=models.CharField(max_length=50, default=' ', null=True, blank=True)
    Maintenance_ID=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.Expenses

class Reservation(models.Model):
    Property_Name = models.ForeignKey(Properties,on_delete=models.CASCADE)
    Customer_Name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Date_From = models.DateTimeField(blank=True, null=True)
    Date_To = models.DateTimeField(blank=True, null=True)
    No_Of_Guest = models.IntegerField(null=True, blank=True)


class Transaction(models.Model):
    Customer_Name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Property_Name = models.ForeignKey(Properties,on_delete=models.CASCADE)
    Trans_Amount= models.ForeignKey(Property_Status,on_delete=models.CASCADE)
    Trans_Time_Date= models.DateTimeField(blank=True, null=True)
    Trans_Type= models.CharField(max_length=50, default=' ', null=True, blank=True)
    Transaction_Token = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Notes = models.CharField(max_length=50, default=' ', null=True, blank=True)


# Create your models here.
from django.db import models

# Create your models here.
