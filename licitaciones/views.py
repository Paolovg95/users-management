from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Licitacion
# Create your views here.

@login_required
# EVENTUALLY ---> READ + UPDATE USING HTMX
def view_my_licitaciones(request):
    # OLP w/ Django-Guardian vs Object specific Query
    licitaciones = Licitacion.objects.filter(empresa=request.user.userprofile.empresa)
    context = {
        'title': 'Mis licitaciones',
        'licitaciones': licitaciones
    }

    return render(request, 'read_my_licitaciones.html', context)

@login_required # This permission allows only subscribed users to see
def view_all_licitaciones(request):
    licitaciones = Licitacion.objects.all()
    context = {
        'title': 'Licitaciones',
        'licitaciones': licitaciones
    }
    return render(request, "read_licitaciones.html", context)

@login_required
def view_licitacion(request, id=None):
    data = {}
    user = request.user
    if id != None:
        licitacion = Licitacion.objects.get(id=id)
        items_solicitados = licitacion.licitacionitem_set.all()
        data['licitacion'] = licitacion

        # SUPERUSER or OWNER of LICITACION can see all the offers
        if user.is_superuser or user == licitacion.owner:
            data['items_solicitados'] = items_solicitados
            ofertas = licitacion.oferta_set.all()
            items_per_offer = {}
            for item in licitacion.licitacionitem_set.all():
                items_per_offer[item.nombre] = {}
                for oferta in ofertas:
                    oferta_item = oferta.ofertaitem_set.filter(licitacion_item=item)
                    if oferta_item:
                        items_per_offer[item.nombre].update({oferta.empresa.nombre: oferta_item[0].price})
                    else:
                        items_per_offer[item.nombre].update({oferta.empresa.nombre:None})
                    # OFERTANTE of OFERTA only
            data['items_per_offer'] = items_per_offer

            oferta = licitacion.oferta_set.filter(empresa=user.userprofile.empresa).first()
            if oferta:
                data['oferta'] = oferta
                prices = {}
                for licitacion_item in items_solicitados:
                    oferta_item = oferta.ofertaitem_set.filter(licitacion_item=licitacion_item).select_related("licitacion_item")
                    if oferta_item:
                        prices[licitacion_item.nombre] = oferta_item[0].price
                    else:
                        prices[licitacion_item.nombre] = None
                data['prices'] = prices
    return render(request, "read_licitacion_detail.html", data)
