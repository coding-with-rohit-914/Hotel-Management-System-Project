from django.contrib import admin

from .models import BookRoomData, FeedbackData, PaymentData, RoomFeedbackData, BillData

class AdminBookRoomData(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'mobile', 'email', 'address', 'room', 'adult', 'children', 'idprrof', 'idprroffile', 'cheakindate', 'cheakintime', 'cheakoutdate', 'cheakouttime', 'timestap']

admin.site.register(BookRoomData, AdminBookRoomData)

class AdminPaymentData(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'mobile', 'email', 'address', 'city', 'state', 'zipcode', 'paymenttype', 'nameascard', 'date', 'time', 'timestap']

admin.site.register(PaymentData, AdminPaymentData)

class AdminBillData(admin.ModelAdmin):
    list_display = ['id', 'bill', 'table', 'room', 'customer', 'mobile', 'address', 'cheakindate', 'cheakintime', 'cheakoutdate', 'cheakouttime', 'decription', 'totalamount', 'gstamount', 'netamount', 'timestap']

admin.site.register(BillData, AdminBillData)

class AdminFeedbackData(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'feedback', 'timestap']

admin.site.register(FeedbackData, AdminFeedbackData)

class AdminRoomFeedbackData(admin.ModelAdmin):
    list_display = ['id','cname', 'cfeedback', 'timestap']

admin.site.register(RoomFeedbackData, AdminRoomFeedbackData)
