from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, CheckoutView

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'order-items', OrderItemViewSet, basename="orderitem")

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('', include(router.urls)),
]
