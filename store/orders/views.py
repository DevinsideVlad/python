from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from orders.forms import OrderForm
from products.models import Basket
from orders.models import Order
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:success')


    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class OrderListView(ListView):
    template_name = 'users/profile.html'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class Success(TemplateView):
    template_name = 'orders/success.html'

# def order(request):
#     if request.method == 'POST':
#         form = OrderForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('products:index'))
#     else:
#         form = OrderForm()
#     context = {'form': form}
#     return render(request, 'orders/order-create.html', context)
