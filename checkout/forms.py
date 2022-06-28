from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('full_name', 'email', 'phone',
                  'address_line1', 'address_line2',
                  'city', 'county', 'country',
                  'postcode', 'shp_full_name',
                  'shp_address_line1', 'shp_address_line2',
                  'shp_city', 'shp_county', 'shp_country',
                  'shp_postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'First name, Surname',
            'email': 'example@email.com',
            'phone': '(optional)',
            'address_line1': 'Example: 42 Church Street',
            'address_line2': '(optional)',
            'city': 'Town or City',
            'county': 'County/State',
            'postcode': 'Postcode/Zipcode',
            'country': 'Country',
            'shp_full_name': 'First name, Surname',
            'shp_address_line1': 'Example: 42 Church Street',
            'shp_address_line2': '(optional)',
            'shp_city': 'Town or City',
            'shp_county': 'County/State',
            'shp_postcode': 'Postcode/Zipcode',
            'shp_country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Adjust labels for full name, address line 1 & 2
            self.fields['full_name'].label = 'Full Name'
            self.fields['address_line1'].label = 'Address Line 1'
            self.fields['address_line2'].label = 'Address Line 2'
            # Manually label shipping address fields
            self.fields['shp_full_name'].label = 'Full Name'
            self.fields['shp_address_line1'].label = 'Address Line 1'
            self.fields['shp_address_line2'].label = 'Address Line 2'
            self.fields['shp_city'].label = 'City'
            self.fields['shp_county'].label = 'County'
            self.fields['shp_postcode'].label = 'Postcode'
            self.fields['shp_country'].label = 'Country'
