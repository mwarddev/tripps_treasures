from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)
from django.contrib import messages
from treasures.models import Treasure


def basket_view(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, treasure_id):
    """ Add a quantity of the specified product to the shopping basket """

    treasure = get_object_or_404(Treasure, pk=treasure_id)
    quantity = int(request.POST.get('treasure_qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'treasure_size' in request.POST:
        size = request.POST['treasure_size']

    basket = request.session.get('basket', {})

    if size:
        if treasure_id in list(basket.keys()):
            if size in basket[treasure_id]['sizeable'].keys():
                basket[treasure_id]['sizeable'][size] += quantity
                messages.success(request, f'{treasure.name} {size} quantity\
                    successfully updated to {basket[treasure_id]["sizeable"][size]}')
            else:
                basket[treasure_id]['sizeable'][size] = quantity
                messages.success(request, f'{treasure.name} {size} successfully\
                     added to the basket.')
        else:
            basket[treasure_id] = {'sizeable': {size: quantity}}
            messages.success(request, f'{treasure.name} {size} successfully\
                 added to the basket.')
    else:
        if treasure_id in list(basket.keys()):
            basket[treasure_id] += quantity
            messages.success(request, f'{treasure.name} quantity\
                successfully updated to {basket[treasure_id]}')
        else:
            basket[treasure_id] = quantity
            messages.success(request, f'{treasure.name}\
                 successfully added to the basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, treasure_id):
    """
    Update size and quantity
    in the shopping basket
    """
    treasure = get_object_or_404(Treasure, pk=treasure_id)
    quantity = int(request.POST.get('treasure_qty'))
    size = None

    if 'treasure_size' in request.POST:
        size = request.POST['treasure_size']

    basket = request.session.get('basket', {})

    if size:
        basket[treasure_id]['sizeable'][size] = quantity
        messages.success(request, f'{treasure.name} quantity updated\
                to {basket[treasure_id]["sizeable"][size]}.\
                ')
    else:
        basket[treasure_id] = quantity
        messages.success(request, f'{treasure.name} quantity updated\
                to {basket[treasure_id]}\
                ')

    request.session['basket'] = basket
    return redirect(reverse('basket_view'))


def delete_from_basket(request, treasure_id):
    """ Remove the item from the shopping bag """

    try:
        treasure = get_object_or_404(Treasure, pk=treasure_id)
        size = None

        if 'treasure_size' in request.POST:
            size = request.POST['treasure_size']

        basket = request.session.get('basket', {})

        if size:
            # Find a way to output messages for multiple size delete
            del basket[treasure_id]['sizeable'][size]
            if not basket[treasure_id]['sizeable']:
                basket.pop(treasure_id)
                messages.success(request, f'{treasure.name} {size}\
                    successfully deleted from your basket.')
        else:
            basket.pop(treasure_id)
            messages.success(request, f'{treasure.name}\
                successfully deleted from your basket.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as exception:
        messages.error(request, f'Error removing item {exception}')
        return HttpResponse(status=500)
