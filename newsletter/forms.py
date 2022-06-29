from django import forms
from .models import Newsletter


class NewsForm(forms.ModelForm):
    """ A form for newsletter registration """
    class Meta:
        model = Newsletter
        fields = ('email_address',)
