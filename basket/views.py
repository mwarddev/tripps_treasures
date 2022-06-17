from django.shortcuts import render, redirect, get_object_or_404
from treasures.models import Treasure


def basket_view(request):
    """ Returns the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, treasure_id):
    """ Add treasure/s to the basket """

    treasure = get_object_or_404(Treasure, pk=treasure_id)
    quantity = int(request.POST.get('treasure_qty'))
    redirect_url = request.POST.get('redirect_url')
    # size = None
    # customise = None
    # personalise = None

    # if 'treasure_size' in request.POST:
    #     size = request.POST['treasure_size']
    basket = request.session.get('basket', {})

    if treasure_id in list(basket.keys()):
        basket[treasure_id] += quantity
    else:
        basket[treasure_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
