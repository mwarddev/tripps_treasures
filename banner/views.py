from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Banner
from .forms import BannerForm


@login_required
def update_banner(request):
    """ Update the info banner """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners\
            can update the banner')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = BannerForm(request.POST)
        if form.is_valid():
            old_banner = Banner.objects.all()
            old_banner.delete()
            form.save()
            messages.success(request, 'Banner successfully updated')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Whooops! banner failed to update.\
                 Please try again.')
    else:
        form = BannerForm()
    template = 'banner/update_info.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
