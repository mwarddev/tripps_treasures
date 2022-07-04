from django import forms
from .models import Banner


class BannerForm(forms.ModelForm):
    """ Gets the info field """
    class Meta:
        model = Banner
        fields = ('info',)
        lables = {
            'info': 'Info Banner'
        }
