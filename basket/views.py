from django.shortcuts import render, redirect, get_object_or_404
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

    # if 'treasure_custom' in request.POST:
    #     if request.POST['treasure_custom'] != '':
    #         customise = request.POST['treasure_custom']

    # if 'treasure_personalise' in request.POST:
    #     if request.POST['treasure_personalise'] != '':
    #         personalise = request.POST['treasure_personalise']

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

    request.session['basket'] = basket
    return redirect(redirect_url)
