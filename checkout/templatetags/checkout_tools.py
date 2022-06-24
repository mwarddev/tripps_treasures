from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate the subtotal in checkout page """
    return price * quantity
