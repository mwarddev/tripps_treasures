from django.shortcuts import render
from django.contrib import messages

from .forms import NewsForm


def news_letter(request):
    """ Get email addresses for newsletter registration """
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully\
                 signed up toour newsletter')
        else:
            messages.error(request, 'Did you enter your email correcty?\
                Please try again.')

    template = 'newsletter/news.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
