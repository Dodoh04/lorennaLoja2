from django.contrib import admin
from .models import Carro, CarroImagem, Lead, Venda


class CarroImagemInline(admin.TabularInline):
    model = CarroImagem
    extra = 3


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    inlines = [CarroImagemInline]
    list_display = ('marca', 'modelo', 'placa', 'km', 'cor', 'data_cadastro')
    list_filter = ('cor', 'marca')
    search_fields = ('marca', 'modelo', 'placa')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'carro', 'origem', 'data_lead')
    search_fields = ('telefone', 'carro__modelo')


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'valor_venda', 'data_venda')
    search_fields = ('cliente', 'carro__modelo')
