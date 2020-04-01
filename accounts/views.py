from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test

from accounts.models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView

from .forms import UserLoginForm,UserCreationForm,CustomerRegistrationForm
from django.urls import reverse

def guest_register(request):
    if request.method == 'POST':
        user_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user, is_customer=True)
            #property = Property.objects.get(apt_no=user_form.cleaned_data['apt_no'])
            #Tenant.objects.create(user=new_user, apt_no=property, lease_start_date=user_form.cleaned_data['lease_start_date'], lease_end_date=user_form.cleaned_data['lease_end_date'])
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = CustomerRegistrationForm()
    return render(request,
                  'accounts/guest/register.html',
                  {'user_form': user_form})

def host_register(request):
    if request.method == 'POST':
        user_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user, is_employee=True)
            #property = Property.objects.get(apt_no=user_form.cleaned_data['apt_no'])
            #Tenant.objects.create(user=new_user, apt_no=property, lease_start_date=user_form.cleaned_data['lease_start_date'], lease_end_date=user_form.cleaned_data['lease_end_date'])
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = CustomerRegistrationForm()
    return render(request,
                  'accounts/host/register.html',
                  {'user_form': user_form})


def maintenance_register(request):
    if request.method == 'POST':
        user_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user, is_maintenanceperson=True)
            #property = Property.objects.get(apt_no=user_form.cleaned_data['apt_no'])
            #Tenant.objects.create(user=new_user, apt_no=property, lease_start_date=user_form.cleaned_data['lease_start_date'], lease_end_date=user_form.cleaned_data['lease_end_date'])
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = CustomerRegistrationForm()
    return render(request,
                  'accounts/maintenance/register.html',
                  {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/home")

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})





