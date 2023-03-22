from django.urls import path
from .views import*


urlpatterns = [
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path("Enroll_summary", CartSummary, name="cart-summary"),
    path("payment-form/",PaymentView.as_view(), name="payment-form"),
    path("others_P/",OtherPaymentView.as_view(), name="others_P"),
    path("order_summary", OrderSummary, name="order-summary"),
    path("order_details/<int:pk>", OrderDetails, name="order-detail"),
    path('remove-form-cart/<slug>/', remove_form_cart, name='remove-form-cart'),
    path('certificate-verification/', certificate_verification, name='certificate-verification'),
    path('certificate-search/', certificate_search, name='certificate-search'),
    path('create_bkash_payment/',create_bkash_payment, name='create_bkash_payment'),
    path('execute_bkash_payment/',execute_bkash_payment, name='execute_bkash_payment'),
]