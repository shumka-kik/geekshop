from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'Админка: пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'Пользователи/Создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'Пользователи/Редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'Пользователи/Удаление'
    user_to_delete = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_to_delete.is_active = False if user_to_delete.is_active else True
        user_to_delete.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {
        'title': title,
        'user_to_delete': user_to_delete
    }
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории/Создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {
        'title': title,
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'Админка: Категории'
    categories_list = ProductCategory.objects.all().order_by('-is_active', 'name')

    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории/Редактирование'
    edit_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {
        'title': title,
        'update_form': edit_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Категории/Удаление'
    category_to_delete = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category_to_delete.is_active = False if category_to_delete.is_active else True
        category_to_delete.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {
        'title': title,
        'category_to_delete': category_to_delete
    }
    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    title = 'Товар/Создание'

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[product_form.category.pk]))
    else:
        product_form = ProductEditForm()

    content = {
        'title': title,
        'update_form': product_form
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = "Админка: Товары"
    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=category.pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': product_list
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = "Админка: Товары"
    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=category.pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': product_list
    }
    return render(request, 'adminapp/product_read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'Товар/Редактирование'
    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {
        'title': title,
        'category': edit_product.category,
        'update_form': edit_form
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'Товар/Удаление'
    product_to_delete = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_to_delete.is_active = False if product_to_delete.is_active else True
        product_to_delete.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {
        'title': title,
        'product_to_delete': product_to_delete
    }
    return render(request, 'adminapp/product_delete.html', content)
