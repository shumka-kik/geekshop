from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def about(request):
    return render(request, 'mainapp/about.html')

def faqs(request):
    return render(request, 'mainapp/faqs.html')

def shoppingcart(request):
    return render(request, 'mainapp/shoppingcart.html')

def checkout(request):
    return render(request, 'mainapp/checkout.html')