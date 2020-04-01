from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *


urlpatterns=[
    path('guest/register', views.guest_register, name="guest_register"),
    path('host/register', views.host_register, name="host_register"),
    path('maintenance/register', views.maintenance_register, name="maintenance_register"),
    path('login/', views.user_login, name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register_done', views.login, name='register_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
