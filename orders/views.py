from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)

    total = sum([item.subtotal() for item in items])

    order = Order.objects.create(
        user=request.user,
        total=total
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    items.delete()

    return redirect('product_list')