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
        data['licitacion'] = licitacion
        # SUPERUSER can see all the offers
        if user.is_superuser:
            ofertas = licitacion.oferta_set.all()
            data['ofertas'] = ofertas
        else:
            oferta = licitacion.oferta_set.filter(empresa=user.userprofile.empresa).first()
            if oferta:
                data['oferta'] = oferta
    return render(request, "read_licitacion_detail.html", data)
