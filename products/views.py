from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Producto creado")
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Producto actualizado")
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Producto eliminado")
    return redirect('product_list')