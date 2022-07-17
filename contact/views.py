from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def view_messages(request):
    """ Get all customer messages """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))
    else:
        cust_messages = Contact.objects.all()
        template = 'contact/messages.html'
        context = {
            'cust_messages': cust_messages,
        }

        return render(request, template, context)


@login_required
def delete_message(request, message_id):
    """ Delete a customer message """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))
    else:
        try:
            message = get_object_or_404(Contact, pk=message_id)
            message.delete()
            messages.success(request, f'Message from {message.cust_name}\
                successfully deleted')

            return redirect(reverse('view_messages'))

        except Exception as exception:
            messages.error(request, f'Unable to delete message {exception}')
            return HttpResponse(status=500)
