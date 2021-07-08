from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)

    else:
        products = Product.objects.all().filter(is_available=True)

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)

    # Podwójne podkreślenie jest dlatego, że category to ForeignKey dla modelu Product,
    # więc szukamy obiektu klasy Product, który spełnia warunek konkretnego slugu
    # oraz przypisany FK Category o slugu category _ _ slug

    # Czyli odwołuje się do własności modelu przypisanego poprzez FK

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,

    }

    return render(request, 'store/product_detail.html', context)
