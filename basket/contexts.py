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

    for treasure_id, treasure_data in basket.items():
        if isinstance(treasure_data, int):
            treasure = get_object_or_404(Treasure(), pk=treasure_id)
            total += treasure_data * treasure.price
            treasure_count += treasure_data
            basket_items.append({
                'treasure_id': treasure_id,
                'quantity': treasure_data,
                'treasure': treasure,
            })
        else:
            treasure = get_object_or_404(Treasure, pk=treasure_id)
            for key, value in treasure_data['treasures_by_size'].items():
                total += treasure.price * value
                treasure_count += value
                basket_items.append({
                    'treasure_id': treasure_id,
                    'quantity': value,
                    'treasure': treasure,
                    'size': key,
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
