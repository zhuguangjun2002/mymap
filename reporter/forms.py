from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Fiberbox


class FiberboxForm(forms.ModelForm):

    class Meta:
        model =  Fiberbox
        fields = ('name', 'town','village','location')
        widgets = { 'location': LeafletWidget() }

