from decimal import Decimal
from django.shortcuts import get_object_or_404
from treasures.models import Treasure


def basket_contents(request):
    """ shopping basket contents processor """

    basket_items = []
    total = 0
    treasure_count = 0
    # basket = request.session.get('basket', {})

    # for item_id, item_data in basket.items():
    #     if isinstance(item_data, int):
    #         treasure = get_object_or_404(Treasure, pk=item_id)
    #         total += item_data * treasure.price
    #         treasure_count += item_data
    #         basket_items.append({
    #             'item_id': item_id,
    #             'quantity': item_data,
    #             'treasure': treasure,
    #         })
    #     else:
    #         treasure = get_object_or_404(Treasure, pk=item_id)
    #         for size, quantity in item_data['items_by_size'].items():
    #             total += quantity * treasure.price
    #             treasure_count += quantity
    #             basket_items.append({
    #                 'item_id': item_id,
    #                 'quantity': quantity,
    #                 'treasure': treasure,
    #                 'size': size,
    #             })

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'treasure_count': treasure_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context