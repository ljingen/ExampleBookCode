from django.shortcuts import render, get_object_or_404
from django.views.generic import View


from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.


def hello(request):
    hell = Product.objects.all()
    print(hell.count())

    return render(request, 'hello.html', {})


class ProductList(View):
    """
    商品列表view
    """
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()  # 所有商品类目

        products = Product.objects.filter(available=True)  # 所有可上架商品

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/product/list.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products})


class ProductDetail(View):
    """
    商品详情页view
    """
    def get(self, request, id, slug):
        print(id)
        print(slug)
        product = get_object_or_404(Product, id=id, slug=slug, available=True)

        cart_product_form = CartAddProductForm()

        return render(request, 'shop/product/detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})

