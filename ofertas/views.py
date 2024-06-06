from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Auth Decorators
from django.contrib.auth.decorators import login_required, permission_required

# Models
from .models import Oferta, OfertaItem
from licitaciones.models import Licitacion

# Forms import
from ofertas.forms import OfertaForm, OfertaItemForm

from django.forms import inlineformset_factory


# Create your views here.
@login_required
@permission_required("ofertas.add_oferta")
def create_offer(request):
    offer_form = OfertaForm()
    OfertaItemFormset = inlineformset_factory(Oferta, OfertaItem, form=OfertaItemForm, extra=1)
    formset = OfertaItemFormset()

    data = {
        'offer_form': offer_form,
        'offer_formset': formset
    }

    return render(request, "create_offer.html", data)
