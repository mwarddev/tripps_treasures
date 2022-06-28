import json
import stripe

from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from treasures.models import Treasure
from user_accounts.forms import UserAccountForm
from user_accounts.models import UserAccount

from basket.contexts import basket_contents
from .forms import PurchaseForm
from .models import Purchase, PurchaseItem


@require_POST
def cache_checkout_data(request):
    """
    Check if user has the save user
    information box checked on form submission 
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as exception:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=exception, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'shp_full_name': request.POST['shp_full_name'],
            'shp_address_line1': request.POST['shp_address_line1'],
            'shp_address_line2': request.POST['shp_address_line2'],
            'shp_city': request.POST['shp_city'],
            'shp_county': request.POST['shp_county'],
            'shp_postcode': request.POST['shp_postcode'],
            'shp_country': request.POST['shp_country'],
        }

        purchase_form = PurchaseForm(form_data)
        if purchase_form.is_valid():
            purchase = purchase_form.save()
            for key, value in basket.items():
                try:
                    treasure = Treasure.objects.get(id=key)
                    if isinstance(value, int):
                        purchase_item = PurchaseItem(
                            purchase=purchase,
                            treasure=treasure,
                            qty=value,
                        )
                        purchase_item.save()
                    else:
                        for size, quantity in value['sizeable'].items():
                            purchase_item = PurchaseItem(
                                purchase=purchase,
                                treasure=treasure,
                                qty=quantity,
                                item_size=size,
                            )
                            purchase_item.save()
                except Treasure.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    purchase.delete()
                    return redirect(reverse('basket_view'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[purchase.purchase_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your basket is empty.")
            return redirect(reverse('home'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                purchase_form = PurchaseForm(initial={
                    'full_name': account.user.get_full_name(),
                    'email': account.user.email,
                    'phone': account.saved_phone,
                    'address_line1': account.saved_address_line1,
                    'address_line2': account.saved_address_line2,
                    'city': account.saved_city,
                    'county': account.saved_county,
                    'postcode': account.saved_postcode,
                    'country': account.saved_country,
                })
            except UserAccount.DoesNotExist:
                purchase_form = PurchaseForm()
        else:
            purchase_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            You forgot to set it in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, purchase_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    purchase = get_object_or_404(Purchase, purchase_number=purchase_number)

    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        # Attach the user's account to the purchase
        purchase.user_account = account
        purchase.save()

    #     # Save the user's info
    #     if save_info:
    #         account_data = {
    #             'default_full_name': purchase.full_name,
    #             'default_phone': purchase.phone,
    #             'default_address_line1': purchase.address_line1,
    #             'default_address_line2': purchase.address_line2,
    #             'default_city': purchase.city,
    #             'default_county': purchase.county,
    #             'default_postcode': purchase.postcode,
    #             'default_country': purchase.country,
    #         }
    #         user_account_form = UserAccountForm(account_data, instance=account)
    #         if user_account_form.is_valid():
    #             user_account_form.save()

    messages.success(request, f'Purchase successfully processed! \
        Your purchase number is {purchase_number}. A confirmation \
        email will be sent to {purchase.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)
