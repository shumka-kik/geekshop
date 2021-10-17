from django.shortcuts import render
import json


# Create your views here.
def main(request):
    with open('static/file_to_load.json') as file:
        data_product = json.load(file)

    with open('static/file_to_load_categories.json') as file:
        data_category = json.load(file)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Main',
        'products': data_product,
        'categories': data_category,
        'links': data_links
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    with open('static/file_to_load.json') as file:
        data_product = json.load(file)

    with open('static/file_to_load_categories.json') as file:
        data_category = json.load(file)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Products',
        'products': data_product,
        'categories': data_category,
        'links': data_links
    }
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Contact',
        'links': data_links
    }
    return render(request, 'mainapp/contact.html', context=content)


def about(request):
    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'About',
        'links': data_links
    }
    return render(request, 'mainapp/about.html', context=content)


def faqs(request):
    with open('static/file_to_load.json') as file:
        data_product = json.load(file)

    with open('static/file_to_load_categories.json') as file:
        data_category = json.load(file)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'FAQs',
        'products': data_product,
        'categories': data_category,
        'links': data_links
    }
    return render(request, 'mainapp/faqs.html', context=content)


def shoppingcart(request):
    with open('static/file_to_load.json') as file:
        data_product = json.load(file)

    with open('static/file_to_load_categories.json') as file:
        data_category = json.load(file)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'ShoppingCart',
        'products': data_product,
        'categories': data_category,
        'links': data_links
    }
    return render(request, 'mainapp/shoppingcart.html', context=content)


def checkout(request):
    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Checkout',
        'links': data_links
    }
    return render(request, 'mainapp/checkout.html', content)
