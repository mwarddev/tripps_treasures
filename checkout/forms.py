from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('full_name', 'email', 'phone',
                  'address_line1', 'address_line2',
                  'city', 'county', 'country',
                  'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'First name, Surname',
            'email': 'example@email.com',
            'phone': '(optional)',
            'city': 'Town or City',
            'street_address1': 'House/Flat Name/Number',
            'street_address2': 'Street name',
            'county': 'County/State',
            'postcode': 'Postcode/Zipcode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # if field != 'country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = True
