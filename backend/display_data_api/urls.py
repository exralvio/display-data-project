from django.urls import path, include

urlpatterns = [
    path('customers/', include('customer.urls')),
    path('orders/', include('order.urls')),
    path('delivery/', include('delivery.urls'))
]
