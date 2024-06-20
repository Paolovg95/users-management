from django.db import models
from users.models import CustomUser
from licitaciones.models import Licitacion, Empresa, LicitacionItem
# Create your models here.

class Oferta(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_oferta = models.IntegerField(null=True)

class OfertaItem(models.Model):
    # Modify in Views to Refer only to Items from that Licitacion
    licitacion_item = models.ForeignKey(LicitacionItem, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    price = models.IntegerField()
