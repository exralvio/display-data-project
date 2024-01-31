from django.urls import path

from order import views

urlpatterns = [
    path('', views.get_orders, name='get_orders')
]
