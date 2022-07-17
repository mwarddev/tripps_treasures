from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


def contact_us(request):
    """ Contact the site owner """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your message has been sent.\
                 We will try to reply to you ASAP.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'It looks like something went wrong.\
                 Please try again.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def view_messages(request):
    """ Get all customer messages """
    messages = Contact.objects.all()
    template = 'contact/messages.html'
    context = {
        'messages': messages,
    }

    return render(request, template, context)
