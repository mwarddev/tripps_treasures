from django import forms
from .models import Purchase, STATUS


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
            'phone': 'Phone number',
            'address_line1': 'Example: 42 Church Street',
            'address_line2': '(optional)',
            'city': 'Town or City',
            'county': 'County/State',
            'postcode': 'Postcode/Zipcode',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]  # noqa
                self.fields[field].widget.attrs['class'] = 'border-secondary'
                # Adjust labels for full name, address line 1 & 2
                self.fields['full_name'].label = 'Full Name'
                self.fields['address_line1'].label = 'Address Line 1'
                self.fields['address_line2'].label = 'Address Line 2'
