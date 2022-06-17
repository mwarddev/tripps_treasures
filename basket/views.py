from django.shortcuts import render


def basket_view(request):
    """ Returns the basket contents page """

    return render(request, 'basket/basket.html')
