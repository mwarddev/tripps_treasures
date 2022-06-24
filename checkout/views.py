from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseForm


def checkout(request):

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket")
        return redirect(reverse('home'))

    purchase_form = PurchaseForm()
    template = 'checkout/checkout.html'
    context = {
        'purchase_form': purchase_form,
    }

    return render(request, template, context)
