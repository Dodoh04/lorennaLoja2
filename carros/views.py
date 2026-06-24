from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Carro, Lead, Venda


def home(request):
    carros = Carro.objects.all().order_by('-data_cadastro')[:6]
    vendas = Venda.objects.select_related('carro').order_by('-data_venda')[:5]
    return render(request, 'index.html', {
        'carros': carros,
        'vendas': vendas,
    })


def lista_carros(request):
    carros = Carro.objects.all().order_by('-data_cadastro')
    return render(request, 'carros/lista.html', {
        'carros': carros,
    })


def detalhe_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    return render(request, 'carros/detalhe.html', {
        'carro': carro,
    })


def criar_lead(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Método inválido.'}, status=405)

    telefone = (request.POST.get('telefone') or '').strip()
    carro_id = request.POST.get('carro_id')
    carro_modelo = (request.POST.get('carro_modelo') or '').strip()

    if not telefone:
        return JsonResponse({'success': False, 'message': 'Informe um telefone para continuar.'}, status=400)

    carro = None
    if carro_id:
        carro = get_object_or_404(Carro, pk=carro_id)

    lead = Lead.objects.create(
        carro=carro,
        telefone=telefone,
        origem='Site',
    )

    return JsonResponse({
        'success': True,
        'message': 'Sua proposta foi enviada com sucesso!',
        'lead_id': lead.pk,
    })


@staff_member_required
def lista_vendas(request):
    vendas = Venda.objects.select_related('carro').order_by('-data_venda')
    return render(request, 'vendas/lista.html', {
        'vendas': vendas,
    })


def sobre_nos(request):
    return render(request, 'sobre_nos.html')