from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from automobileapp.models import *
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *
from automobileapp.models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.db.models import F
from django.db.models import Q
from django.http import JsonResponse, HttpResponse


@login_required
def add_to_cart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    order_course, created = CartItem.objects.get_or_create(course=course, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order course is in the order
        if order.cart_items.filter(course__slug=course.slug).exists():
            # messages.info(request, 'This course already add to cart')
            return redirect('payment-form')
        
        else:
            order.cart_items.add(order_course)
            # messages.info(request, 'This course was add to cart')
            return redirect('payment-form')
    else:
        ordered_date = timezone.now()
        order =Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.cart_items.add(order_course)
        # messages.info(request, "This course was add to cart")
        return redirect("payment-form")
    return redirect("payment-form")


    course = get_object_or_404(Course, slug=slug)
    order_course, created = CartItem.objects.get_or_create(course=course, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check the order course is in the order
        if order.cart_items.filter(course__slug=course.slug).exists():
            # messages.info(request, 'This course already add to cart')
            return redirect('/')
        
        else:
            order.cart_items.add(order_course)
            # messages.info(request, 'This course was add to cart')
            return redirect('/')
    else:
        ordered_date = timezone.now()
        order =Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.cart_items.add(order_course)
        # messages.info(request, "This course was add to cart")
        return redirect("/")
    return redirect("/")


@login_required
def CartSummary(request):
    try:
        order =Order.objects.get(user=request.user, ordered=False)
        # form = CouponCodeForm(request.POST or None)
        context={
            'order':order,
            # 'form':form,
        }
        return render(request, 'enrolled/cart_summary.html', context)
    
    except ObjectDoesNotExist:
        return redirect('/')


class PaymentView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            form = OrderPaymentForm()
            payment_method = PaymentMethodForm()
            order = Order.objects.get(user=request.user, ordered=False)
            course = Course.objects.get(slug=slug)
           


            context = {
                'form': form,
                'payment_method': payment_method,
                'order':order,
                'course':course,
                
            }
            return render(request, 'enrolled/payment.html', context)
        except ObjectDoesNotExist:
            messages.warning(request, 'You have no active order')
            return redirect('/')


    def post(self, request, *args, **kwargs):
        order_payments  = OrderPayment.objects.all()
        tsn_list =[]
        for i in order_payments:
            tsn_list.append(i.pyamnet_transaction_id)
        print(tsn_list)

        form = OrderPaymentForm(request.POST)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)
        
        if request.method == 'post' or request.method == 'POST':
            form = OrderPaymentForm(request.POST)
            pay_form = PaymentMethodForm(request.POST, instance=payment_obj)
            if form.is_valid() and pay_form.is_valid():

                payment_method =form.cleaned_data.get('payment_method')
                your_payment_number =form.cleaned_data.get('your_payment_number')
                pyamnet_transaction_id =form.cleaned_data.get('pyamnet_transaction_id')

                order_payment  = OrderPayment(
                    user=request.user,
                    payment_method=payment_method,
                    your_payment_number=your_payment_number,
                    pyamnet_transaction_id=pyamnet_transaction_id
                )
                order_payment.save()
                pay_method = pay_form.save()

                if pay_method.payment_option == 'Bkash' or pay_method.payment_option == 'Nagad' or pay_method.payment_option == 'Roket':
                    if pay_method.payment_option == order_payment.payment_method:
                        order_qs = Order.objects.filter(user=request.user, ordered=False)
                        order = order_qs[0]
                        order.ordered = True
                        order.orderId = order.id
                        order.total_order_amount = order.get_total()
                        order.paymentId = pay_method.payment_option
                        
                        order.save()
                        messages.info(request, "You order was successful")
                        return redirect('/')
                    else:
                        messages.info(request, "payment method not matching")
                        return redirect('payment-form')
            return redirect('payment-form')

@login_required
def OrderSummary(request):
    try:
        order =Order.objects.filter(user=request.user, ordered=True)
        context={
            'order':order,
        }
        return render(request, 'enrolled/order_summary.html', context)
    
    except ObjectDoesNotExist:
        return redirect('/')

def OrderDetails(request,pk):
    order = Order.objects.get(pk=pk)
    order_items = CartItem.objects.filter(order=order)
    context={
            'order':order,
            'order_items':order_items,
        }
    return render(request, 'enrolled/order_details.html',context)

def remove_form_cart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0] 
        #check in the order item is in cart
        if order.cart_items.filter(course__slug=course.slug).exists():
            order_item = CartItem.objects.filter(user=request.user, ordered=False)[0]
            order_item.delete()
            messages.info(request, 'This Course was remove from cart')
            return redirect('payment-form')
        else:
            #user dose not have
            messages.info (request, 'This Course was not your cart')
            return redirect('payment-form')
    else:
        #user dose not have
        messages.info (request, 'This Course was not your cart')
        return redirect('payment-form')


def certificate_verification(request):
    return render(request, 'enrolled/certificate-verification.html')

def certificate12(request):
    return render(request, 'enrolled/certificate.html')    

 

def certificate_search(request):
    query = request.GET['q']
    search_item = Q(certificate_id__icontains=query) 
    certificate = StudentCertificateVerification.objects.filter(search_item)
    return render(request, 'enrolled/certificate-search.html', {'certificate':certificate})


def bookInStudent(request, slug):
    obj = get_object_or_404(Course, slug=slug)

    if request.method == 'POST':
        forms = bookingstudentFrom(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = bookingstudentFrom()
    

        context = {
            'forms':forms,
            'obj':obj
        }

    return render(request, 'enrolled/others_pay.html',context)







import requests
import json
from django.views.decorators.csrf import csrf_exempt
app_key = "4f6o0cjiki2rfm34kfdadl1eqq"
app_secret = "2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b"

@csrf_exempt
def grant_token_function():
    token_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/token/grant"
    payload = {
    "app_key":f"{app_key}",
    "app_secret":f"{app_secret}"
    }

    headers = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "username":"sandboxTokenizedUser02",
        "password":"sandboxTokenizedUser02@12345"
    }

    token_response = requests.post(token_url, json=payload, headers=headers)
    token = json.loads(token_response.content)
    # print(token)
    id_tokens = token.get('id_token')
    return id_tokens




@login_required
@csrf_exempt
def create_bkash_payment(request, *args, **kwargs):
    id_token = grant_token_function()
    create_url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/create"
    order = Order.objects.get(user=request.user, ordered=False)
    payload = json.dumps({
        "mode": "0011",
        "payerReference": "N/A",
        "callbackURL":"http://localhost:8000/execute_bkash_payment/",
        "amount": "1",
        "currency": "BDT",
        "intent": "sale",
        "merchantInvoiceNumber": f"{order.id}"
    })

    headers = {
        "Accept": "application/json",
        "Authorization": f"{id_token}",
        "X-APP-Key":f"{app_key}",
        "Content-type": "application/json"
    }

    create_response = requests.post(create_url, data=payload, headers=headers)
    response = json.loads(create_response.content)
    print(response,"create response")
   
    paymentId=response['paymentID']
    createTime=response['paymentCreateTime']
    transactionStatus = response['transactionStatus']
    amount = response['amount']
    currency = response['currency']
    intent = response['intent']
    merchantInvoiceNumber = response['merchantInvoiceNumber']
    
    BkashPayment.objects.create(user=request.user, paymentID=paymentId, createTime=createTime, transactionStatus=transactionStatus , amount=amount, currency=currency,  intent=intent, merchantInvoiceNumber=merchantInvoiceNumber)
 

    return redirect(response['bkashURL'])
 
 
@login_required
@csrf_exempt
def execute_bkash_payment(request):
    id_token = grant_token_function()
    length = BkashPayment.objects.filter(user=request.user).count()
    Id = BkashPayment.objects.filter(user=request.user)[length-1].paymentID 
    url = "https://tokenized.sandbox.bka.sh/v1.2.0-beta/tokenized/checkout/execute"

    payload = {
        "paymentID":f"{Id}",
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"{id_token}",
        "X-APP-Key": f"{app_key}",
    }

    response_create = requests.post(url, json=payload, headers=headers)
    response = json.loads(response_create.content)
    print(response,"execute response")

    if response.get("statusCode") == "0000" and response.get("statusMessage") == "Successful":
        trxID=response.get('trxID')
        print(trxID)
        paymentID=response.get('paymentID')
        print(paymentID)

        paymentID=response.get('paymentID')
        createTime=response.get('paymentExecuteTime')
        trxID = response.get('trxID')
        transactionStatus = response.get('transactionStatus')
        amount = response.get('amount')
        currency = response.get('currency')
        intent = response.get('intent')
        merchantInvoiceNumber = response.get('merchantInvoiceNumber')
        customerMsisdn = response.get('customerMsisdn')

        BkashPaymentExecute.objects.create(user=request.user, paymentID=paymentID, createTime=createTime, trxID=trxID, transactionStatus=transactionStatus , amount=amount, currency=currency,  intent=intent, merchantInvoiceNumber=merchantInvoiceNumber, customerMsisdn=customerMsisdn)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order = order_qs[0]
        order.ordered = True
        order.orderId = order.id
        order.payment_option = 'Bkash'

        order_items = CartItem.objects.filter(user=request.user, ordered=False)
        for order_item in order_items:
            order_item.ordered = True
            order_item.save()

        order.save()
        messages.success(request, "Your Payment successful done")
        return redirect("/")

    elif response.get("statusCode") == "2023" and response.get("statusMessage") == "Insufficient Balance":
        messages.success(request, "Insufficient Balance")
        return redirect("payment-form")

    else:
        messages.success(request, "Your Payment Failed")
        return redirect("payment-form")

    




