from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _ # Translates according to users’ language preferences.
from django.core.validators import RegexValidator

from .managers import CustomUserManager

class Empresa(models.Model):
    PARAGUAY = "PY"
    BRASIL = "BR"
    ARGENTINA = "AR"
    URUGUAY = "UR"
    CHILE = "CH"
    PAISES = {
        PARAGUAY: "Paraguay",
        BRASIL: "Brasil",
        ARGENTINA: "Argentina",
        URUGUAY: "Uruguay",
        CHILE: "Chile",
    }

    direccion_validator = RegexValidator(regex=r'^[a-zA-Z0-9!@#$&()\\-`.+,/\]*$', message="Direccion", code="invalid_address")
    web_validator = RegexValidator(regex=r'^[a-zA-Z0-9!@#$&()\\-`.+,/\]*$', message="Web", code="invalid_web_address")

    ruc = models.BigIntegerField()
    razon_social = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=220, validators=[direccion_validator])
    pais = models.CharField(max_length=3, choices=PAISES, default=PARAGUAY)
    email = models.EmailField(max_length=254)
    web = models.CharField(max_length=100, validators=[web_validator])
    descripcion = models.TextField(max_length=220)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    # celular = models.IntegerField(max_digits=10)
    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField(max_length=50)
    # empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
# Create your models here.
