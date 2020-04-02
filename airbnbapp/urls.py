from django.urls import path, re_path
from .import views

app_name = 'airbnbapp'

urlpatterns=[
    path('',views.base,name='base'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('property/<id>/', views.propertyview, name='propertyview'),
    path('contact/', views.contact, name='contact'),
    path('bookings/<id>/', views.viewbookings, name='viewbookings'),
    path('cancel/<id>/', views.cancelbooking, name='cancelbooking'),
    re_path(r'^home/AddProperty', views.AddProperty, name='Addproperty'),
    path('property/update/<id>', views.AddProperty, name='updateproperty'),
    path('property/addmaintenace/<id>', views.addmaintenance, name='addmaintenance'),
    path('property/delete/<id>', views.deleteproperty, name='deleteproperty'),
    re_path(r'^home/$', views.home, name='home'),

]