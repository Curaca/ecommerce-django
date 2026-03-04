from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem
from products.models import Product

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum([item.subtotal() for item in items])
    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        item.quantity += 1
        item.save()

    messages.success(request, "Producto agregado al carrito")
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.success(request, "Producto eliminado")
    return redirect('cart_view')