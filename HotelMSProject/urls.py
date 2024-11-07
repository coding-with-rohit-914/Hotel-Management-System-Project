"""HotelMSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HotelMSApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.slide,name='slide'),

    #-------- Admin -----------------------------------------------
    path('adminsignup',views.AdminSignupPage,name='adminsignup'),
    path('adminlogin/',views.AdminLoginPage,name='adminlogin'),
    path('adminlogout/',views.AdminLogoutPage,name='adminlogout'),
    path('adminhome/',views.AdminHomePage,name='adminhome'),

    #----- User -----------------------------------
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',views.HomePage,name='home'),

    #--------------------------------------------------------
    path('hotel/',views.hotel,name='hotel'),
    path('booking/',views.booking,name='booking'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('notification/',views.notification,name='notification'),
    path('roomfeedback/',views.roomfeedback,name='roomfeedback'),
    path('bill/',views.bill,name='bill'),
    path('paymentpage/',views.paymentpage,name='paymentpage'),
    path('roombook/',views.roombook,name='roombook'),
    path('roomstatus/',views.roomstatus,name='roomstatus'),
    path('viewbooking/',views.viewbooking,name='viewbooking'),
    path('updatebooking/<id>',views.updatebooking,name='updatebooking'),
    path('updatebookingdata/<id>', views.updatebookingdata, name='updatebookingdata'),
    path('deletebooking/<id>', views.deletebooking, name='deletebooking')
]
