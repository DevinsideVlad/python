from django.urls import path, include

from products.views import products, basket_add, about, product_page
app_name = 'products'

urlpatterns = [
  path('', products, name='index'),
  path('category/<int:category_id>/', products, name='category'),
  path('page/<int:page_number>/', products, name='paginator'),
  path('filter/<int:filter_id>', products, name='filter'),
  path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
  path('about/', about, name='about'),
  path('product_page/<int:product_id>/', product_page, name='product_page'),
  # path('quantity_input/<int:product_id>/', quantity_input, name='quantity_input'),
]
