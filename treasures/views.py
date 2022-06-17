from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Treasure, Category


def all_treasures(request):
    """ Returns all products including queries """

    # treasures = Treasure.objects.prefetch_related('images')
    treasures = Treasure.objects.all()

    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treasures = treasures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                # messages.error(request, 'No search criteria entered')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            treasures = treasures.filter(queries)

    template_name = 'treasures/treasures.html'
    context = {
        'treasures': treasures,
        'selected_categories': categories,
        'search_query': query,
    }

    return render(request, template_name, context)


def full_details(request, treasure_id):
    """ Full details for an individual treasure """
    treasure = get_object_or_404(Treasure, pk=treasure_id)

    while True:
        random_treasure = Treasure.objects.filter(category=treasure.category).order_by('?').first()
        if random_treasure != treasure:
            related = random_treasure
            break

    template_name = 'treasures/full_details.html'

    context = {
        'treasure': treasure,
        'related': related,
    }

    return render(request, template_name, context)
