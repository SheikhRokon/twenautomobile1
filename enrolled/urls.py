from django.urls import path
from . views import*
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path("Enroll_summary", CartSummary, name="cart-summary"),
    # path("payment-form/<slug>/", login_required(PaymentView.as_view()), name="payment-form"),
    path("payment-form/<slug>/", payment_view, name="payment-form"),
    path("order_summary", OrderSummary, name="order-summary"),
    path("order_details/<int:pk>", OrderDetails, name="order-detail"),
    path('remove-form-cart/<slug>/', remove_form_cart, name='remove-form-cart'),

    path('certificate/', certificate12, name='certificate'),
    path('certificate-verification/', certificate_verification, name='certificate-verification'),
    path('certificate_verification_result/', certificate_verification_result, name='certificate_verification_result'),
    path('certificate-search/', certificate_search, name='certificate-search'),
    path('create_bkash_payment/<slug>/',create_bkash_payment, name='create_bkash_payment'),
    path('execute_bkash_payment/',execute_bkash_payment, name='execute_bkash_payment'),
    path('<slug>', bookInStudent, name='bookInStudent'),
    # path('order-create/<slug>/', order_create, name="order_create")
]