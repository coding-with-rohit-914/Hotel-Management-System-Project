from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import  BookRoomData, FeedbackData, RoomFeedbackData, PaymentData, BillData

#-------------------- Slider Page --------------------
def slide(request):
    return render (request,'slide.html')

#===============================================================================

#-------------------- Admin Signup Page --------------------
def AdminSignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('adminlogin')
    return render (request,'adminsignup.html')

#-------------------- Admin Login Page--------------------
def AdminLoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('adminhome')
        else:
            return HttpResponse ("Username or Password is incorrect, Please Cheak your Username or Password otherwise Create a New Account?")
    return render (request,'adminlogin.html')

#-------------------- Admin Logout Page --------------------
def AdminLogoutPage(request):
    logout(request)
    return redirect('slide')

#-------------------- Admin Home Page --------------------
@login_required(login_url='adminlogin')
def AdminHomePage(request):
    return render (request,'adminhome.html')

#===============================================================================

#-------------------- User Signup Page--------------------
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

#-------------------- User Login Page--------------------
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect, Please Cheak your Username or Password otherwise Create a New Account?")
    return render (request,'login.html')

#-------------------- User Logout Page --------------------
def LogoutPage(request):
    logout(request)
    return redirect('slide')

#-------------------- Hotel Gallery Page --------------------
@login_required(login_url='login')
def hotel(request):
    return render (request,'hotel.html')

#-------------------- User Home Page --------------------
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

#-------------------- Booking Page --------------------
@login_required(login_url='login')
def booking(request):
    return render (request,'booking.html')

#-------------------- Booking Room Status Page --------------------
@login_required(login_url='login')
def roomstatus(request):
    return render (request,'roomstatus.html')

#-------------------- Room Booking Page --------------------
@login_required(login_url='login')
def roombook(request):
    if request.method == 'GET':
        return render(request, 'roombook.html')
    else:
        BookRoomData(
        fullname = request.POST.get('Full_Name'),
        mobile = request.POST.get('Mobile_No'),
        email = request.POST.get('Email_ID'),
        address = request.POST.get('Address'),
        room = request.POST.get('Room_Type'),
        adult = request.POST.get('No_Of_Adult'),
        children = request.POST.get('No_Of_Children'),
        idprrof = request.POST.get('ID_Proof_Type'),
        idprroffile = request.POST.get('ID_Proof_File'),
        cheakindate = request.POST.get('Check_In_Date'),
        cheakintime = request.POST.get('Check_In_Time'),
        cheakoutdate = request.POST.get('Check_Out_Date'),
        cheakouttime = request.POST.get('Check_Out_Time')
        ).save()
        return redirect('roombook')

#-------------------- View Booking Page --------------------
@login_required(login_url='login')
def viewbooking(request):
    data = BookRoomData.objects.all()
    return render(request, 'viewbooking.html',{'data':data})

#-------------------- Update Booking Page --------------------
@login_required(login_url='login')
def updatebooking(request, id):
    row = BookRoomData.objects.get(id=id)
    return render(request, 'updatebooking.html', {'row':row})

#-------------------- Update Booking Page --------------------
@login_required(login_url='login')
def updatebookingdata(request, id):
    data = BookRoomData.objects.get(id=id)
    data.fullname = request.POST.get('Full_Name')
    data.mobile = request.POST.get('Mobile_No')
    data.email = request.POST.get('Email_ID')
    data.address = request.POST.get('Address')
    data.room = request.POST.get('Room_Type')
    data.adult = request.POST.get('No_Of_Adult')
    data.children = request.POST.get('No_Of_Children')
    data.idprrof = request.POST.get('ID_Proof_Type')
    data.idprroffile = request.POST.get('ID_Proof_File')
    data.cheakindate = request.POST.get('Check_In_Date')
    data.cheakintime = request.POST.get('Check_In_Time')
    data.cheakoutdate = request.POST.get('Check_Out_Date')
    data.cheakouttime = request.POST.get('Check_Out_Time')
    data.save()
    return redirect('viewbooking')

#-------------------- Delete Booking Page --------------------
@login_required(login_url='adminlogin')
def deletebooking(request, id):
    data = BookRoomData.objects.get(id=id)
    data.delete()
    return redirect('viewbooking')

#-------------------- Bill Page --------------------
@login_required(login_url='adminlogin')
def bill(request):
    if request.method == 'GET':
        return render(request, 'bill.html')
    else:
        BillData(
        bill = request.POST.get('inv_no'),
        table = request.POST.get('table_no'),
        room = request.POST.get('room_no'),
        customer = request.POST.get('cust_na'),
        mobile = request.POST.get('mo_no'),
        address = request.POST.get('addr'),
        cheakindate = request.POST.get('cheak_in_date'),
        cheakintime = request.POST.get('cheak_in_time'),
        cheakoutdate = request.POST.get('cheak_out_date'),
        cheakouttime = request.POST.get('cheak_out_time'),
        decription = request.POST.get('item_nm'),
        # quntity = request.POST.get('qty'),
        # rate = request.POST.get('rate'),
        # amount = request.POST.get('amt'),
        totalamount = request.POST.get('total_amt'),
        gstamount = request.POST.get('gst_amt'),
        netamount = request.POST.get('net_amt')
        ).save()
        return redirect('bill')

#-------------------- Payment Page --------------------
@login_required(login_url='adminlogin')
def paymentpage(request):
    if request.method == 'GET':
        return render(request, 'paymentpage.html')
    else:
        PaymentData(
        fullname = request.POST.get('Full_Name'),
        mobile = request.POST.get('Mo_No'),
        email = request.POST.get('Email_ID'),
        address = request.POST.get('Address'),
        city = request.POST.get('City'),
        state = request.POST.get('State'),
        zipcode = request.POST.get('Zip_Code'),
        date = request.POST.get('Date'),
        time = request.POST.get('Time'),
        paymenttype = request.POST.get('Payment_Type'),
        nameascard = request.POST.get('Name_On_Card')
        ).save()
        return redirect('paymentpage')

#-------------------- Services Page --------------------
@login_required(login_url='login')
def services(request):
    return render (request,'services.html')

#-------------------- Contact Page --------------------
@login_required(login_url='login')
def contact(request):
    if request.method == 'GET':
        fbs = FeedbackData.objects.all()
        return render(request, 'contact.html', {'fbs':fbs})
    else:
        fb = request.POST.get('contact')
        FeedbackData(
        name = request.POST.get('Name'),
        email = request.POST.get('Email'),
        subject = request.POST.get('Subject'),
        feedback = request.POST.get('Feedback')
        ).save()
        fbs = FeedbackData.objects.all()
        return render(request, 'contact.html', {'fbs':fbs})

#-------------------- Feedback Notification Page --------------------
@login_required(login_url='login')
def notification(request):
    if request.method == 'GET':
        fbs = FeedbackData.objects.all()
        return render(request, 'notification.html', {'fbs':fbs})
    else:
        fb = request.POST.get('contact')
        FeedbackData(
        name = request.POST.get('Name'),
        email = request.POST.get('Email'),
        subject = request.POST.get('Subject'),
        feedback = request.POST.get('Feedback')
        ).save()
        fbs = FeedbackData.objects.all()
        return render(request, 'contact.html', {'fbs':fbs})

#-------------------- Room Feedback Page --------------------
@login_required(login_url='login')
def roomfeedback(request):
    if request.method == 'GET':
        fbs = RoomFeedbackData.objects.all()
        return render(request, 'roomfeedback.html', {'fbs':fbs})
    else:
        fb = request.POST.get('roomfeedback')
        RoomFeedbackData(
        cname = request.POST.get('cname'),
        cfeedback = request.POST.get('cfeedback')
        ).save()
        fbs = RoomFeedbackData.objects.all()
        return render(request, 'roomfeedback.html', {'fbs':fbs})
