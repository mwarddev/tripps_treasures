from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Treasure, Category
from .forms import TreasureForm


def all_treasures(request):
    """ Returns all products including queries """

    treasures = Treasure.objects.prefetch_related('images')
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
                messages.error(request, 'No search criteria entered')
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
        random_treasure = Treasure.objects.filter(category=treasure.category)\
                            .order_by('?').first()
        if random_treasure != treasure:
            related = random_treasure
            break

    template_name = 'treasures/full_details.html'

    context = {
        'treasure': treasure,
        'related': related,
    }

    return render(request, template_name, context)


@login_required
def add_treasure(request):
    """ Add new products """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = TreasureForm(request.POST, request.FILES)
        if form.is_valid():
            treasure = form.save()
            messages.success(request, 'You successfully added a treasure!')
            return redirect(reverse('full_details', args=[treasure.id]))
        else:
            messages.error(request, 'Whooops! We failed to add treasure.\
                 Please ensure the form is valid')
    else:
        form = TreasureForm()
    template = 'treasures/add_treasure.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_treasure(request, treasure_id):
    """ Edit a treasure in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    treasure = get_object_or_404(Treasure, pk=treasure_id)
    if request.method == 'POST':
        form = TreasureForm(request.POST, request.FILES, instance=treasure)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated treasure!')
            return redirect(reverse('full_details', args=[treasure.id]))
        else:
            messages.error(request, 'Whooops! We failed to update\
                 the treasure. Please ensure the form is valid')
    else:
        form = TreasureForm(instance=treasure)
        messages.info(request, f'You are editing {treasure.name}')
    template = 'treasures/edit_treasure.html'
    context = {
        'form': form,
        'treasure': treasure,
    }

    return render(request, template, context)


@login_required
def delete_treasure(request, treasure_id):
    """ Delete a treasure """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    treasure = get_object_or_404(Treasure, pk=treasure_id)
    treasure.delete()
    messages.success(request, f'{treasure.name} deleted!')
    return redirect(reverse('home'))
