from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M95KPHuFsjfect1zj8MxqaNJxkPb1dKOp4KbTv5cl5XeD3ep4U70rz7TXms0p5tIoBdbIF8PbHK5b1RsB4O28Hn00sQwtcDZi',
        'client_secret': 'test_client_secret',
    }
    print(context)
    print(context['stripe_public_key'])
    print(context['client_secret'])

    return render(request, template, context)