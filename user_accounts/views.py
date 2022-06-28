from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Purchase
from .models import UserAccount
from .forms import UserAccountForm


@login_required
def account(request):
    """ Display the user's profile. """
    user_account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully updated.')
        else:
            messages.error(request, 'Update failed.\
                 Please ensure the form is valid.')
    else:
        form = UserAccountForm(instance=user_account)
    purchases = user_account.purchases.all()

    template = 'user_accounts/user_account.html'
    context = {
        'user_account': user_account,
        'form': form,
        'purchases': purchases,
        'on_user_account_page': True
    }

    return render(request, template, context)

def purchase_history(request, purchase_number):
    """ Get user's purchase history """
    purchase = get_object_or_404(Purchase, purchase_number=purchase_number)

    messages.info(request, (
        f'This is a past confirmation for purchase number {purchase_number}. '
        'A confirmation email was sent on the purchase date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
        'from_user_account': True,
    }

    return render(request, template, context)
