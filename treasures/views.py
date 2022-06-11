from django.shortcuts import render
from .models import Treasure, Category, Image


def all_treasures(request):
    """ Returns all products including queries """

    # treasures = Treasure.objects.prefetch_related('images')
    treasures = Treasure.objects.all()

    # query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treasures = treasures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    template_name = 'treasures/treasures.html'
    context = {
        'treasures': treasures,
        'selected_categories': categories,
    }

    return render(request, template_name, context)
