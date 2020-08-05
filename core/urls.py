from django.urls import path
from .views import HomeView, ItemDetailView, CheckoutView, add_to_cart, remove_from_cart, OrderSummaryView, \
    remove_single_item_from_cart, PaymentView, AddCouponView, RequestRefundView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<slug>', ItemDetailView.as_view(), name='products'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>', PaymentView.as_view(), name="payment"),
    path('request-refund', RequestRefundView.as_view(), name="request-refund")
]