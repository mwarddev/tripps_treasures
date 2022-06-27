from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from treasures.models import Treasure


def basket_contents(request):
    """ shopping basket contents processor """

    basket_items = []
    total = 0
    treasure_count = 0
    basket = request.session.get('basket', {})
    for key, value in basket.items():
        if isinstance(value, int):
            treasure = get_object_or_404(Treasure, pk=key)
            total += value * treasure.price
            treasure_count += value
            basket_items.append({
                'treasure_id': key,
                'treasure': treasure,
                'quantity': value,
            })
        else:
            treasure = get_object_or_404(Treasure, pk=key)
            for size, quantity in value['sizeable'].items():
                total += quantity * treasure.price
                treasure_count += quantity
                basket_items.append({
                    'treasure_id': key,
                    'treasure': treasure,
                    'size': size,
                    'quantity': quantity,
                })

    delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'treasure_count': treasure_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
