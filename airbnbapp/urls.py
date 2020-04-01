from django.urls import path, re_path
from .import views

app_name = 'airbnbapp'

urlpatterns=[
    path('',views.base,name='base'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('property/<id>/', views.propertyview, name='propertyview'),
    path('contact/', views.contact, name='contact'),
    path('bookings/<id>/', views.viewbookings, name='viewbookings'),
    path('bookings/<id>/<bid>/', views.cancelbooking, name='cancelbooking'),
    path('bookings/<id>/<name>/', views.viewproperty, name='viewproperty'),
    path('bookings/<id>/<name>/', views.viewproperty, name='viewproperty'),
    re_path(r'^home/AddProperty', views.AddProperty, name='Addproperty'),
    path('property/<id>', views.AddProperty, name='updateproperty'),
    path('property/delete/<id>', views.deleteproperty, name='deleteproperty'),
    path('search/', views.search, name='search'),
    path('property/reserve/<id>/', views.reserve, name='reserve'),
    re_path(r'^home/$', views.home, name='home'),

]