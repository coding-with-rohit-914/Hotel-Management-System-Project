from django.db import models

class PaymentData(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    paymenttype = models.CharField(max_length=30)
    nameascard = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Payment From' + self.fullname

class BookRoomData(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    room = models.CharField(max_length=30)
    adult = models.IntegerField()
    children = models.IntegerField()
    idprrof = models.CharField(max_length=30)
    idprroffile = models.ImageField()
    cheakindate = models.DateField()
    cheakintime = models.TimeField()
    cheakoutdate = models.DateField()
    cheakouttime = models.TimeField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Book Room From' + self.fullname

class BillData(models.Model):
    bill = models.IntegerField()
    table = models.IntegerField()
    room = models.IntegerField()
    customer = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    cheakindate = models.DateField()
    cheakintime = models.TimeField()
    cheakoutdate = models.DateField()
    cheakouttime = models.TimeField()
    decription = models.CharField(max_length=50)
    # quntity = models.IntegerField()
    # rate = models.IntegerField()
    # amount = models.IntegerField()
    totalamount = models.IntegerField()
    gstamount = models.IntegerField()
    netamount = models.IntegerField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Bill From' + self.customer

class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    feedback = models.TextField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Feedback From' + self.name

class RoomFeedbackData(models.Model):
    cname = models.CharField(max_length=50)
    cfeedback = models.TextField()
    timestap = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Feedback From' + self.cname
