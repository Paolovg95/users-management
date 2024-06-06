from django.db import models
from users.models import Empresa, CustomUser
# Create your models here.
class Licitacion(models.Model):
    titulo = models.CharField(max_length=50)
    obs = models.TextField(max_length=300)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'licitacion'
        verbose_name_plural = 'licitaciones'
        permissions = [('can_view_all_licitaciones', 'Can view licitaciones only users that subscribed.')]


class LicitacionItem(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    price = models.IntegerField()
