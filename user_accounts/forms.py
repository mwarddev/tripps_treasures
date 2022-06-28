from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'saved_full_name': 'First name, Surname',
            'saved_phone': '(optional)',
            'saved_address_line1': 'Example: 42 Church Street',
            'saved_address_line2': '(optional)',
            'saved_city': 'Town or City',
            'saved_county': 'County/State',
            'saved_postcode': 'Postcode/Zipcode',
            'saved_country': 'Country',
        }

        self.fields['saved_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Adjust labels for full name, address line 1 & 2
            self.fields['saved_full_name'].label = 'Full Name'
            self.fields['saved_address_line1'].label = 'Address Line 1'
            self.fields['saved_address_line2'].label = 'Address Line 2'