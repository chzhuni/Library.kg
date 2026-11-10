from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from orders.forms import OrderForm
# CREATE
def create_order_view(request):
    if request.method == "POST":
        form_order = OrderForm(request.POST, request.FILES)
        if form_order.is_valid():
            form_order.save()
            return redirect('order_list')
    else:
        form_order = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form_order})


# READ
def order_list_view(request):
    if request.method == 'GET':
        order_list = Order.objects.all().order_by('-id')
        return render(request, 'orders/order_list.html', {'orders': order_list})


# UPDATE
def update_order_view(request, id):
    order_id = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form_order = OrderForm(request.POST, request.FILES, instance=order_id)
        if form_order.is_valid():
            form_order.save()
            return redirect('order_list')
    else:
        form_order = OrderForm(instance=order_id)
    return render(request, 'orders/update_order.html', {'form': form_order, 'order_id': order_id})


# DELETE
def delete_order_view(request, id):
    order_id = get_object_or_404(Order, id=id)
    order_id.delete()
    return redirect('order_list')