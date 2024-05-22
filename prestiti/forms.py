from django import forms
from .models import Prestito
from datetime import datetime, timedelta

class ConfermaPrestito(forms.ModelForm):
    class Meta:
        model = Prestito
        fields = ['data_inzio']

    def __init__(self, *args, **kwargs):
        super(ConfermaPrestito, self).__init__(*args, **kwargs)
        # Set the default value for 'data_inzio' to today
        self.fields['data_inzio'].initial = datetime.now().date()

