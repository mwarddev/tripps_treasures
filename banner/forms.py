from django import forms
from .models import Banner


class BannerForm(forms.ModelForm):
    """ Gets the info field """
    class Meta:
        model = Banner
        fields = ('info',)

    def __init__(self, *args, **kwargs):
        """ Adjust BannerForm fields """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-secondary'
            self.fields[field].widget.attrs['placeholder'] = 'Please enter the\
                 info banner text here.'
            self.fields['info'].label = False
