from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
  return render(request, 'store/cart/summary.html')


def cart_add(request):
  cart = Cart(request)
  if request.method == 'POST':
    item_id = int(request.POST.get('item_id'))
    item = get_object_or_404(Product, id=item_id)
    cart.add(item=item)
    response = JsonResponse({'test': 'data'})
    return response

