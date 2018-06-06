from django import forms
from .models import Fiberbox


class FiberboxForm(forms.ModelForm):

    class Meta:
        model =  Fiberbox
        fields = ('name', 'town','village')

