from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Properties,Reservation,Property_Availability,Reservation
from django.contrib.auth.decorators import login_required
from .forms import PropertiesForm,AddMaintenanceForm
from .filters import propertyfilter
from accounts.models import CustomUser
from accounts.forms import UserLoginForm
import datetime



from django.shortcuts import render_to_response

def base(request):
    props = Properties.objects.all()
    availability = Property_Availability.objects.all()
    reservation = Reservation.objects.all()
    context = {'props': props}
    if request.method == 'GET':
        county = request.GET.get('Location')
        adult = request.GET.get('adult')
        child = request.GET.get('child')
        check_in=request.GET.get('date_min')
        check_out=request.GET.get('date_max')

        if county is not None and county != "":
            property_list = Properties.objects.filter(County=county )& Properties.objects.filter(Adults__gte=adult )& Properties.objects.filter(Children__gte=child )
            context = {'property_list': property_list}
            return render(request, 'airbnbapp/property_list.html', context)

        else:
            return render(request, "base.html", context)

        return render(request, "base.html", context)

    else:
       return render(request,"base.html",context)

def propertyview(request,id):
    context={'property_list':Properties.objects.get(pk=id)}
    print("request",request.method)
    if request.method == 'GET':
        print(request.GET)
        from_date = request.GET.get('checkin')
        to_date = request.GET.get('checkout')
        prop = Properties.objects.get(pk=id)
        propid=id
        userid=request.user
        print ("user is",userid)


        if from_date is not None and from_date != '' :

                reservation = Reservation()
                reservation.Date_From = datetime.datetime.strptime(from_date, "%m/%d/%Y").strftime('%Y-%m-%d')
                reservation.Date_To = datetime.datetime.strptime(to_date, "%m/%d/%Y").strftime('%Y-%m-%d')
                reservation.Property_Name = Properties.objects.get(pk=propid)
                if request.user.is_authenticated:
                     reservation.Customer_Name = CustomUser.objects.get(username=userid)
                     reservation.save()
                     reserve_id = reservation.id
                     prop = Properties.objects.get(pk=propid)
                     reserve = Reservation.objects.get(pk=reserve_id)
                     context = {'prop': prop, 'reserve': reserve}
                     return render(request, "airbnbapp/reserve.html", context)
                else:
                     form = UserLoginForm()
                     return render(request, 'accounts/login.html', {'form': form})

        else:
                return render(request, "airbnbapp/propertyview.html", context)

    else:
       return render(request,"airbnbapp/propertyview.html",context)



def aboutus(request):
    props=Properties.objects.all()
    return render(request, 'airbnbapp/aboutus.html',{'props': props})

def contact(request):
    props=Properties.objects.all()
    return render(request, 'airbnbapp/contact.html',{'props': props})

def viewbookings(request,id):
    bookings=Reservation.objects.filter(Customer_Name=id).select_related('Property_Name')

    return render(request, 'airbnbapp/bookingsview.html',{'bookings': bookings})


def cancelbooking(request,id):
    bookings=Reservation.objects.get(pk=id)
    bookings.delete()
    return redirect('/home')


def viewproperty(request,name,id):
    property_list=Properties.objects.get(Property_Name=name)
    return render(request,"airbnbapp/propertyview.html",{'property_list': property_list})

def AddProperty(request,id=0):
    if request.method=="GET":
        if id==0:
          form=PropertiesForm()
        else:
          property=Properties.objects.get(pk=id)
          form=PropertiesForm(instance=property)

        return render(request, 'airbnbapp/Addproperty.html', {'form': form})

    else:
        if id==0:
            form=PropertiesForm(request.POST)
        else:
            property=Properties.objects.get(pk=id)
            form=PropertiesForm(request.POST,instance=property)


        if form.is_valid():
            print('printing post', request.POST)
            form.save()
        else:
            # Do something in case if form is not valid
            raise Http404

        return redirect('/home')

def deleteproperty(request,id=0):
    property = Properties.objects.get(pk=id)
    property.delete()
    return redirect('/home')


def addmaintenance(request,id):
    if request.method == 'GET':
        form = AddMaintenanceForm(initial={'Property_Name': id})
        return render(request, 'airbnbapp/addmaintenance.html', {'form': form})

    else:
        form = AddMaintenanceForm(request.POST)
        if form.is_valid():
            print('printing post', request.POST)
            form.save()
            return redirect('/home')


@login_required
def home(request):
    current_user = request.user
    if(current_user.profile.is_customer):
        props = Properties.objects.all()
        return render(request, 'airbnbapp/guesthome.html',{'props': props})
    elif(current_user.profile.is_employee):
        props = Properties.objects.filter(Property_Host=current_user.id).select_related('Property_Host')
        form = PropertiesForm()
        context = {'props':props, 'form':form}
        return render(request, 'airbnbapp/hosthome.html',context)
    elif (current_user.profile.is_maintenanceperson):
        props = Properties.objects.all()
        return render(request, 'airbnbapp/maintenancepersonhome.html',{'props': props})

