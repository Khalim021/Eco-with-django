from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from orders.forms import OrderModelForm
from products.models import ProductModel


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'checkout.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('orders:history')

    def form_valid(self, form):
        products = ProductModel.get_from_cart(self.request)
        form.instance.user = self.request.user
        form.instance.price = ProductModel.get_from_cart(
            self.request
        ).aggregate(Sum('real_price'))['real_price__sum']

        order = form.save()

        order.products.set(products)
        order.save()

        self.request.session['cart'] = []
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = ProductModel.get_from_cart(self.request)
        context['profile'] = self.request.user.profile

        return context


class OrderHistoryListView(LoginRequiredMixin, ListView):
    template_name = 'youshop_list.html'

    def get_queryset(self):
        return self.request.user.orders.all()
