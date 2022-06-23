from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)
from django.contrib import messages
from treasures.models import Treasure


def basket_view(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, treasure_id):
    """ Add a quantity of the specified product to the shopping bag """

    treasure = get_object_or_404(Treasure, pk=treasure_id)
    quantity = int(request.POST.get('treasure_qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # customise = 'N/A'
    # personalise = 'N/A'

    if 'treasure_size' in request.POST:
        size = request.POST['treasure_size']

    # basket = request.session.get('basket', {'sizes': {}, 'no_sizes': {}})
    basket = request.session.get('basket', {})

    # if size:
    #     if treasure_id in list(basket['sizes'].keys()):
    #         if size in basket['sizes'][treasure_id]['size']:
    #             if customise in basket['sizes'][treasure_id]['customise']:
    #                 if personalise in basket['sizes'][treasure_id]['personalise']:
    #                     basket['sizes'][treasure_id]['quantity'] += quantity
    #                 else:
    #                     basket['sizes'][treasure_id]['quantity'] = quantity
    #             else:
    #                 basket['sizes'] = {treasure_id: {'size': size,'quantity': quantity, 'customise': customise, 'personalise': personalise}}
    #         else:
    #             basket['sizes'] = {treasure_id: {'size': size,'quantity': quantity, 'customise': customise, 'personalise': personalise}}
    #     else:
    #         basket['sizes'] = {treasure_id: {'size': size,'quantity': quantity, 'customise': customise, 'personalise': personalise}}
    # else:
    #     if treasure_id in list(basket.keys()):
    #         basket[treasure_id] += quantity
    #     else:
    #         basket[treasure_id] = quantity

    # if size:
    #     basket['sizes'][treasure_id] = {'quantity': quantity, 'size': size, 'customise': customise, 'personalise': personalise}
    # else:
    #     basket['no_sizes'][treasure_id] = {'quantity': quantity, 'customise': customise, 'personalise': personalise}

    if size:
        if treasure_id in list(basket.keys()):
            if size in basket[treasure_id]['treasures_by_size'].keys():
                basket[treasure_id]['treasures_by_size'][size] += quantity
            else:
                basket[treasure_id]['treasures_by_size'][size] = quantity
        else:
            basket[treasure_id] = {'treasures_by_size': {size: quantity}}
    else:
        if treasure_id in list(basket.keys()):
            basket[treasure_id] += quantity
        else:
            basket[treasure_id] = quantity
            messages.success(request, f'{treasure.name} successfully added to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, treasure_id):
    """ 
    Update size, quantity, and add customisations and
    personalisation in the shopping basket 
    """
    quantity = int(request.POST.get('treasure_qty'))
    size = None
    # customise = 'N/A'
    # personalise = 'N/A'

    if 'treasure_size' in request.POST:
        size = request.POST['treasure_size']
    
    # if 'treasure_custom' in request.POST:
    #     customise = request.POST['treasure_custom']

    # if 'treasure_personalise' in request.POST:
    #     personalise = request.POST['treasure_personalise']

    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[treasure_id]['treasures_by_size'][size] = quantity
            # messages.success(
            #     request, f'Updated size {size.upper()} {product.name} \
            #         quantity to {basket[item_id]["items_by_size"][size]}'
            #     )
        else:
            del basket[treasure_id]['treasures_by_size'][size]
            if not basket[treasure_id]['treasures_by_size']:
                basket.pop(treasure_id)
            # messages.success(
            #     request, f'Removed size {size.upper()} {product.name} \
            #         from your bag'
            #     )
    else:
        if quantity > 0:
            basket[treasure_id] = quantity
            # messages.success(
            #     request, f'Updated {product.name} quantity to {bag[item_id]}'
            #     )
        else:
            basket.pop(treasure_id)
            # messages.success(request, f'Removed {product.name} from your bag')

    # if customise:
    #     basket[treasure_id][customise]['treasures_by_size'][size] = quantity
    #     # messages.success(
    #     #     request, f'Updated size {size.upper()} {product.name} \
    #     #         quantity to {basket[item_id]["items_by_size"][size]}'
    #     #     )
    # else:
    #     basket[treasure_id][customise] = quantity

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
            del basket[treasure_id]['treasures_by_size'][size]
            if not basket[treasure_id]['treasures_by_size']:
                basket.pop(treasure_id)
            # messages.success(
            #     request,
            #     f'Removed size {size.upper()} {product.name} from your bag'
            #     )
        else:
            basket.pop(treasure_id)
            # messages.success(request, f'Removed {product.name} from your bag')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        # messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
