from django.db import models
from django.conf import settings
from automobileapp.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class CartItem(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    ordered = models.BooleanField(default=False) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
        
    # def saving_price(self):
    #     return (self.item.price * self.quantity) - (self.item.discount_price * self.quantity)

    # def saving_percent(self):

    #     return (self.saving_price()) / (self.item.price * self.quantity) * 100

    def get_subtotal(self):
        if self.course.course_discount_price:
            return self.course.course_discount_price * self.quantity
        else:
            return self.course.course_price * self.quantity

    def __str__(self):
        return self.course.title


Order_Status = (
    ('pending','pending'),
    ('processing','processing'),
    ('unpaid','unpaid'),
    ('paid','paid'),
)

class Order(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    cart_items = models.ManyToManyField(CartItem)
    # order_status = models.CharField(max_length = 150, choices=Order_Status , default='pending')
    total_order_amount = models.CharField(max_length = 150, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    orderId = models.CharField(max_length = 150, blank=True, null=True)
    paymentId = models.CharField(max_length = 150, blank=True, null=True) 
    # coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    payment_option = models.CharField(max_length = 150)
    course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name ='order_to_course',null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_complate_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username   

    def get_total(self):
        total = 0
        for i in self.cart_items.all():
            total += i.get_subtotal()
        return total

    # def get_total_with_shiping_charge(self):
    #     total = 0
    #     for i in self.items.all():
    #         total += i.get_subtotal()
    #     total += self.shiping_charge
    #     return total

    # def get_total_with_coupon(self):
    #     total = 0 
    #     for i in self.items.all():
    #         total += i.get_subtotal()
    #     total += self.shiping_charge
    #     total -= self.coupon.amount
    #     return total

    # def total(self):
    #     if self.coupon:
    #         return self.get_total_with_coupon()
    #     else:
    #         return self.get_total_with_shiping_charge()

class Coupon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(default=timezone.now)
    max_value = models.IntegerField(validators=[MaxValueValidator(100)], verbose_name='Coupon Quantity', null=True) # No. of coupon
    used = models.IntegerField(default=0)
    
    def __str__(self):
        return self.code

    # def get_coupon_update_url(self):
    #     return reverse('coupon-update', kwargs={'pk': self.pk})

Payment_method = (
    ('Bkash', 'Bkash'),
    ('Nagad', 'Nagad'),
    ('Roket', 'Roket'),
)

class OrderPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    payment_method  = models.CharField(max_length = 150, choices=Payment_method)
    your_payment_number  = models.CharField(max_length = 12)
    pyamnet_transaction_id  = models.CharField(max_length = 150)

    def __str__(self):
        return self.user.username + ' / ' + self.your_payment_number
    

class StudentCertificateVerification(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course  = models.ForeignKey(Course,on_delete=models.SET_NULL, blank=True, null=True)
    certificate = models.FileField(upload_to='StudentCertificate')
    certificate_id = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.student.username + ' / ' + self.course.title

class BkashPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True , null=True)
    paymentID = models.CharField(max_length = 150)
    createTime = models.CharField(max_length = 150)
    orgName = models.CharField(max_length = 150)
    transactionStatus = models.CharField(max_length = 150)
    amount = models.CharField(max_length = 150)
    currency = models.CharField(max_length = 150)
    intent = models.CharField(max_length = 150)
    merchantInvoiceNumber = models.CharField(max_length = 150)
    course  = models.CharField(max_length=255, blank=True, null=True)
    # course  = models.ForeignKey(Course,on_delete=models.SET_NULL, blank=True, null=True)




class BkashPaymentExecute(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True , null=True)
    paymentID = models.CharField(max_length=150)
    createTime = models.CharField(max_length=150)
    trxID = models.CharField(max_length=150)
    transactionStatus = models.CharField(max_length=150)
    amount = models.CharField(max_length=150)
    currency = models.CharField(max_length=150)
    intent = models.CharField(max_length=150)
    merchantInvoiceNumber = models.CharField(max_length=150)
    customerMsisdn = models.CharField(max_length=150)
    course  = models.CharField(max_length=255, blank=True, null=True)



class BokingNow(models.Model):

    name = models.CharField(max_length=80)
    email = models.EmailField(max_length = 250)
    phone= models.CharField(max_length = 13)
    course_titel = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    tentative_admission_date = models.CharField(max_length=200, blank=True, null=True)
    ins_org = models.CharField(max_length=200,blank=True, null=True)

    class Meta:

        verbose_name = 'BokingNow'
        verbose_name_plural = 'BokingNows'

    def __str__(self):
        return self.name


