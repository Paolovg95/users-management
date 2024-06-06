from django.contrib import admin
from .models import Licitacion, LicitacionItem
from ofertas.models import Oferta, OfertaItem
# Register your models here.

class LicitacionItemInline(admin.StackedInline):
    model = LicitacionItem
    extra = 0
    fields = ['nombre','price']

class OfertaInline(admin.StackedInline):
    model = Oferta
    extra = 0
    readonly_fields = ['owner', 'empresa']

@admin.register(Licitacion)
class LicitacionAdmin(admin.ModelAdmin):
    inlines = [LicitacionItemInline, OfertaInline]
    list_display = ('titulo', 'id')
