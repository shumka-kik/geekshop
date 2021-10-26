from django.shortcuts import render, get_object_or_404
import json

from basketapp.models import Basket
from .models import Product, ProductCategory


# Create your views here.
def main(request):
    # with open('static/file_to_load.json') as file:
    #     data_product = json.load(file)
    new_product = Product.objects.all().order_by('id')[:4]
    popular_product = Product.objects.all().order_by('-price')[:4]
    count_basket_products = get_count_products_in_basket(request)

    # with open('static/file_to_load_categories.json') as file:
    #     data_category = json.load(file)
    data_category = ProductCategory.objects.all()

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Main',
        'new_products': new_product,
        'popular_product': popular_product,
        'categories': data_category,
        'count_basket_products':count_basket_products,
        'links': data_links
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    count_basket_products = get_count_products_in_basket(request)

    # Если в урле задан идентификатор категории, то необходимо фильтрануть товары по категории,
    # иначе выводим все товары
    if pk is not None:
        if pk == 0:
            data_product = Product.objects.all().order_by('price')
            current_category = {'name': 'Все игрушки'}
        else:
            current_category = get_object_or_404(ProductCategory, pk=pk)
            data_product = Product.objects.filter(category__pk=pk)
    else:
        data_product = Product.objects.all().order_by('price')
        current_category = {'name': 'Все игрушки'}

    data_category = ProductCategory.objects.all()

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Products',
        'products': data_product,
        'categories': data_category,
        'current_category': current_category,
        'count_basket_products': count_basket_products,
        'links': data_links
    }
    return render(request, 'mainapp/products.html', context=content)


def productdetail(request, id):
    count_basket_products = get_count_products_in_basket(request)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    if id is not None or id == 0:
        if id == 0:
            data_category = ProductCategory.objects.all()
            data_product = Product.objects.all()
            current_category = {'name': 'Все игрушки'}

            content = {
                'title': 'Products',
                'products': data_product,
                'categories': data_category,
                'current_category': current_category,
                'count_basket_products': count_basket_products,
                'links': data_links
            }
            return render(request, 'mainapp/products.html', context=content)
        else:
            product = get_object_or_404(Product, pk=id)
            current_category = product.category.name
    else:
        data_category = ProductCategory.objects.all()
        data_product = Product.objects.all()
        current_category = {'name': 'Все игрушки'}

        content = {
            'title': 'Products',
            'products': data_product,
            'categories': data_category,
            'current_category': current_category,
            'count_basket_products': count_basket_products,
            'links': data_links
        }
        return render(request, 'mainapp/products.html', context=content)

    data_category = ProductCategory.objects.all()

    # В качестве рекоммендуемых берем простова товары из той же категории что и просматриваемый товар
    recommend_products = Product.objects.filter(category__pk=product.category.pk)

    content = {
        'title': 'ProductDetail',
        'product': product,
        'recommend_products': recommend_products,
        'categories': data_category,
        'current_category': current_category,
        'count_basket_products': count_basket_products,
        'links': data_links
    }

    return render(request, 'mainapp/productdetail.html', context=content)


def contact(request):
    data_category = ProductCategory.objects.all()
    count_basket_products = get_count_products_in_basket(request)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Contact',
        'links': data_links,
        'categories': data_category,
        'count_basket_products': count_basket_products,
    }
    return render(request, 'mainapp/contact.html', context=content)


def about(request):
    count_basket_products = get_count_products_in_basket(request)

    data_category = ProductCategory.objects.all()
    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'About',
        'links': data_links,
        'categories': data_category,
        'count_basket_products': count_basket_products,
    }
    return render(request, 'mainapp/about.html', context=content)


def faqs(request):
    # with open('static/file_to_load.json') as file:
    #     data_product = json.load(file)
    popular_product = Product.objects.all().order_by('-price')[:4]
    data_category = ProductCategory.objects.all()
    count_basket_products = get_count_products_in_basket(request)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'FAQs',
        'popular_product': popular_product,
        'categories': data_category,
        'links': data_links,
        'count_basket_products': count_basket_products,
    }
    return render(request, 'mainapp/faqs.html', context=content)


def shoppingcart(request):
    # with open('static/file_to_load.json') as file:
    #     data_product = json.load(file)
    data_product = Product.objects.all()
    popular_product = Product.objects.all().order_by('-price')[:4]
    count_basket_products = get_count_products_in_basket(request)

    # with open('static/file_to_load_categories.json') as file:
    #     data_category = json.load(file)
    data_category = ProductCategory.objects.all()

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'ShoppingCart',
        'products': data_product,
        'popular_product': popular_product,
        'categories': data_category,
        'links': data_links,
        'count_basket_products': count_basket_products,
    }
    return render(request, 'mainapp/shoppingcart.html', context=content)


def checkout(request):
    count_basket_products = get_count_products_in_basket(request)
    data_category = ProductCategory.objects.all()
    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Checkout',
        'links': data_links,
        'categories': data_category,
        'count_basket_products': count_basket_products,
    }
    return render(request, 'mainapp/checkout.html', content)

def get_count_products_in_basket(request):
    # Товары в корзине, отображаем количество в хэдере
    count_basket_products = 0

    if request.user.is_authenticated:
        count_basket_products = len(Basket.objects.filter(user=request.user))

    return count_basket_products
