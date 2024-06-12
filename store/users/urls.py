from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users.views import login, registration, logout, WebPasswordResetView, profile
from orders.views import OrderListView

app_name = 'users'

urlpatterns = [
  path('login/', login, name='login'),
  path('registration/', registration, name='registration'),
  path('profile/', profile, name='profile'),
  path('logout/', logout, name='logout'),
  path("password_reset/", WebPasswordResetView.as_view(), name="password_reset"),
  # path("password_reset/success/", WebPasswordResetDone.as_view(), name="password_reset_success"),
  path('profile/', OrderListView.as_view(), name="orders_list"),

]
