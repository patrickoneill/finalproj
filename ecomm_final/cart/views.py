from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from merch.models import Category, Product
from .models import Cart, CartItem

# Create your views here.
def cart(request):
    return render(request, 'cart.html')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=product_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
                    )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quntity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart
            )
        cart_item.save()

    return redirect('cart_detail')

def cart_detail(request, total=0, counter=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cart.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter)) 
