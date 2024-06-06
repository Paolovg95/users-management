from django import forms
from .models import Oferta, OfertaItem

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = "__all__"

class OfertaItemForm(forms.ModelForm):
    class Meta:
        model = OfertaItem
        fields = ['nombre', 'price']
