from django.urls import path, include

from orders.views import OrderCreateView, Success

app_name = 'orders'

urlpatterns = [
   path('order-create/', OrderCreateView.as_view(), name='order-create'),
   path('success/', Success.as_view(), name='success'),
   # path('order-create/', order, name='order-create')
]
