from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import index
# from store.admin import admin_site
from django.contrib import admin

admin.site.site_header = 'Панель администрации'  # default: "Django Administration"
admin.site.index_title = 'Админ панель'
admin.site.site_title = 'Пользователь'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('account/', include("django.contrib.auth.urls")),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
