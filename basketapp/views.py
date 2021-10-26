from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import json

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def basket(request):
    popular_product = Product.objects.all().order_by('-price')[:4]
    data_category = ProductCategory.objects.all()
    count_basket_products = get_count_products_in_basket(request)
    basket_products = []
    basket_summ = 0

    if request.user.is_authenticated:
        basket_products = Basket.objects.filter(user=request.user)
        basket_summ = sum(bask.quantity * bask.product.price for bask in basket_products)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Корзина',
        'popular_product': popular_product,
        'basket_products': basket_products,
        'categories': data_category,
        'count_basket_products': count_basket_products,
        'basket_summ':basket_summ,
        'links': data_links
    }
    return render(request, 'basketapp/shoppingcart.html', content)

def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)

    if basket:
        basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_count_products_in_basket(request):
    # Товары в корзине, отображаем количество в хэдере
    count_basket_products = 0

    if request.user.is_authenticated:
        count_basket_products = len(Basket.objects.filter(user=request.user))

    return count_basket_products