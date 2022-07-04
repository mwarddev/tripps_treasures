from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Banner
from .forms import BannerForm


def show_info(request):
    """ Shows the info banner message """
    banners = Banner.objects.all()

    template = 'templates/base.html'
    context = {
        'banners': banners,
    }

    return redirect(request, template, context)


@login_required
def update_banner(request):
    """ Update the info banner """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners\
            can update the banner')
        return redirect(reverse('home'))
    if request.method == 'POST':
        banner_form = BannerForm(request.POST)
        if banner_form.is_valid():
            old_banner = Banner.objects.all()
            old_banner.delete()
            banner_form.save()
            messages.success(request, 'Banner successfully updated')
            return redirect(reverse('home'))
        else:
            banner_form = BannerForm()
            messages.error(request, 'Whooops! banner failed to update')
    else:
        banner_form = BannerForm()
    template = 'banner/update_info.html'
    context = {
        'banner_form': banner_form,
    }

    return render(request, template, context)
