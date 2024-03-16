from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
#                 cart.clear()
#             return render(request, 'orders/order/created.html', {'order': order})
#         else:
#             form = OrderCreateForm()
#         return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
    
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # order_created(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            # return redirect(reverse('payment:payment_process'))
            return render(request,'payment/process.html',{'order': order})
        return render(request,'orders/created.html',{'order': order})
    else:
        form = OrderCreateForm()
    return render(request,'orders/create.html',{'cart': cart, 'form': form})


