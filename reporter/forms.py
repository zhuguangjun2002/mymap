from django import forms
from .models import FiberBox


class FiberBoxForm(forms.ModelForm):

    class Meta:
        model =  FiberBox
        fields = ('name', 'town')
