from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import View


from shop.models import Product
from coupons.models import Coupon

from coupons.forms import CouponApplyForm
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
class AddToCartView(View):
    """
    创建一个添加物品到购物车视图
    """
    def post(self, request, product_id):
        #  搞了一个Cart的实例，主要是在request.session里面添加一个cart
        cart = Cart(request)
        # 根据product_id，取出对应的产品
        product = get_object_or_404(Product, id=product_id)
        # 获取添加商品的数量和是否更新
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            #  向缓存里面添加一条数据
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            # 定位到购物车详情页
            return redirect('cart:cart_detail')


class RemoveFromCartView(View):
    """
    从购物车删除商品的视图
    """
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(View):
    """
    购物车详情页
    """
    def get(self, request):
        # 从request.session里面取出来 cart数据
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})

            coupon_apply_form = CouponApplyForm()
        return render(request, 'cart/detail.html', {'cart': cart,
                                                    'coupon_apply_form': coupon_apply_form})
