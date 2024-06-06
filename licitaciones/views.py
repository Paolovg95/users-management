from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Licitacion
# Create your views here.

@login_required
@permission_required("licitaciones.view_licitacion")
# EVENTUALLY ---> READ + UPDATE USING HTMX
def view_my_licitaciones(request):
    # OLP w/ Django-Guardian vs Object specific Query
    licitaciones = Licitacion.objects.filter(empresa=request.user.userprofile.empresa)
    context = {
        'title': 'Mis licitaciones',
        'licitaciones': licitaciones
    }

    return render(request, 'mi-listado.html', context)

@login_required # This permission allows only subscribed users to see
def view_all_licitaciones(request):
    licitaciones = Licitacion.objects.all()
    context = {
        'title': 'Licitaciones',
        'licitaciones': licitaciones
    }
    return render(request, "licitaciones.html", context)

@login_required
@permission_required("licitaciones.view_licitacion")
def view_licitacion(request, id=None):
    if id != None:
        licitacion = Licitacion.objects.get(id=id)
        ofertas = licitacion.oferta_set.all()
        data = {
            'licitacion': licitacion,
            'ofertas': ofertas
        }
        return render(request, "mi_licitacion.html", data)
