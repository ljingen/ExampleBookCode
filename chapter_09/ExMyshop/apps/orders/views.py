# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import View

from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm
# Create your views here.


class CreateOrderView(View):
    """
    从购物车点击那个CheckOut，将会进入这个视图,直接请求我们将给他返回一个填写订单的表单
    """
    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm()
        # return HttpResponse('这是一个页面')
        return render(request, 'orders/create.html', {'cart': cart,
                                                      'form': form})

    def post(self, request):
        cart = Cart(request)  # 初始化购物车，从session里面将cart取出来
        form = OrderCreateForm(request.POST)  # 从页面表单里,把数据取出来
        if form.is_valid():
            order = form.save(commit=False)  # 保存数据，生成订单;

            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()

            for item in cart:  # 把购物车里面的商品都跟订单绑定起来
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
        # clear the cart
        cart.clear()
        return render(request, 'orders/created.html', {'order': order})
