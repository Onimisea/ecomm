from django.shortcuts import get_object_or_404, render

from .models import Category, Subcategory, Product


def all_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def categories_list(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'store/products/categories.html', {'categories': categories, 'subcategories': subcategories})


def subcategory_list(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    
    products = Product.objects.filter(category=category).filter(subcategory=subcategory)

    return render(request, 'store/products/subcategory.html', {'category': category, 'subcategory': subcategory, 'products': products })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
