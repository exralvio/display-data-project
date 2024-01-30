from django.urls import path, include

urlpatterns = [
    path('customer/', include('customer.urls')),
    path('order/', include('order.urls')),
    path('delivery/', include('delivery.urls'))
]
