from django import forms
from .models import Licitacion, LicitacionItem

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = "__all__"
class LicitacionItemForm(forms.ModelForm):
    class Meta:
        model = LicitacionItem
        fields = "__all__"
