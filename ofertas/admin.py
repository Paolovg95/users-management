from django.contrib import admin
from .models import Oferta, OfertaItem
# Register your models here.

class OfertaItemInline(admin.StackedInline):
    model = OfertaItem
    extra = 0
    fields = ['nombre', 'price','licitacion_item']

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    inlines = [OfertaItemInline]
    list_display = ('id', )
