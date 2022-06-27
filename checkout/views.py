from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseForm
from basket.contexts import basket_contents

import stripe


def checkout(request):

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket")
        return redirect(reverse('home'))
    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    # stripe.api_key = stripe_secret_key
    # intent = stripe.PaymentIntent.create(
    #     amount=stripe_total,
    #     currency=settings.STRIPE_CURRENCY,
    # )

    purchase_form = PurchaseForm()
    template = 'checkout/checkout.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': 'pk_test_51KobbhKUeIBJskAgLEI6ieO0zXUai2rm8RH3pQNTCl8C75PKZLGllmVEX3dh9pdzqFQmm0Ya93C0JYqdKFYhMQUM00NwH2XCo4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
