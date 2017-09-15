# -*- coding: utf-8 -*-
from decimal import Decimal

from django.conf import settings

from shop.models import Product
from coupons.models import Coupon


class Cart(object):
    """
    购物车对象,管理购物车的添加、删除、保存、迭代、长度、清空
    """
    def __init__(self, request):
        """
        Initialize the cart.
        """
        # store current applied coupon
        self.session = request.session

        self.coupon_id = self.session.get('coupon_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Let's create a method to add products to the cart or update their quantity. 
        Add the following add() and save() methods to the Cart class
        :param product:商品实例,The Product instance to add or update in the cart
        :param quantity:要添加到购物车的商品数量,An optional integer for product quantity. This defaults to 1
        :param update_quantity:是否更新数量，默认为FalseThis is a boolean that indicates whether the quantity needs to be 
        updated with the given quantity (True), or the new quantity has to be added to the existing quantity (False)
        :return: None
        """
        product_id = str(product.id)
        # 如果商品的id不在cart字典里面
        if product_id not in self.cart:
            # 如果这个商品 不在字典里面我们需要在字典里面添加一条新的字典记录,个数先初始化为0
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        # 如果需要更新商品数量,则更新商品数量
        if update_quantity:
            # 如果需要更新数量，代表是前段手动设置了数量，此时直接 当前商品数量=更改后的quantity
            self.cart[product_id]['quantity'] = quantity
        else:
            # 如果变更状态为False，那么 直接原来的这字段加上新的quantity
            self.cart[product_id]['quantity'] += quantity

        # 调用自己的保存函数
        self.save()

    def save(self):
        """
        更新在session里面的cart
        :return: 
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        #  mark the session as modified ,to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.从购物车删除一个商品
        :param product: 要移除的商品实例
        :return: 
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
       from the database.
        :return: 
        """
        product_ids = self.cart.keys() # 从字典里面取出所有的key
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart
        :return:  all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # return the sum of the quantities of all the cart items.
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
