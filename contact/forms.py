from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ A form for messaging the site owner """
    class Meta:
        model = Contact
        fields = ('cust_name', 'email_address', 'purchase_number', 'message',)
        labels = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-secondary'
            # Add placeholders
            self.fields['cust_name'].widget.attrs['placeholder'] = 'Your name here'  # noqa
            self.fields['email_address'].widget.attrs['placeholder'] = 'example@example.com'  # noqa
            self.fields['purchase_number'].widget.attrs['placeholder'] = '(optional)'  # noqa
            self.fields['message'].widget.attrs['placeholder'] = 'Your message here'  # noqa
            # Change label name
            self.fields['cust_name'].label = 'Customer name'
