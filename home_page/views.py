from django.shortcuts import render


def home(request):
    """ Returns the index page """

    return render(request, 'home_page/index.html')
