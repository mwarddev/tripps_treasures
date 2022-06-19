from django.shortcuts import render, redirect


def basket_view(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, treasure_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('treasure_qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'treasure_size' in request.POST:
        size = request.POST['treasure_size']
    basket = request.session.get('basket', {})

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
