from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import Empresa
from vagas.models import Vagas
from .forms import FormEmpresa
from vagas.forms import FormVagas
from usuarios.models import Empregador
from django.http import JsonResponse
# from django.views.decorators.http import require_GET    

import requests
import json


def consulta_cnpj_ajax(request):
    import requests

    cnpj = request.GET.get('cnpj', None)
    if not cnpj:
        return JsonResponse({'error': 'CNPJ não fornecido'}, status=400)

    url = f"https://open.cnpja.com/office/{str(cnpj)}"  # Substitua pela URL real da API

    response = requests.get(url)

    if response.status_code == 200:
        try:
            # Desserializa o JSON em um dicionário Python
            data = response.json()  # Garante que `data` é um dicionário
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Erro ao processar os dados da API'}, status=500)

        nome_fantasia = data.get('alias', '')
        endereco = data.get('address', {}).get('street', '') + ', ' + data.get('address', {}).get('number', '')
        email = data.get('emails', [{}])[0].get('address', '')
        caracteristica_empresa = data.get('mainActivity', {}).get('text', '')

        return JsonResponse({
            'nome': nome_fantasia,
            'endereco': endereco,
            'email': email,
            'caracteristica_empresa':caracteristica_empresa,
        })
    else:
        return JsonResponse({'error': 'Erro ao consultar API'}, status=response.status_code)
    
            
def nova_empresa(request):
    if request.method == "POST":
        formEmpresa = FormEmpresa(request.POST, request.FILES)
        if formEmpresa.is_valid():
            nova_empresa = formEmpresa.save()
            empregador = Empregador.objects.get(cpf=request.session['empregador_id'])
            empregador.empresa = nova_empresa
            empregador.save()

            messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
            return redirect('/vagas/vagas_empregador')  
        else:
            print(formEmpresa.errors)                                                                                                

    else:
        formEmpresa = FormEmpresa()

    context = {
        'form': formEmpresa,
    }
    return render(request, 'nova_empresa.html', context)
        
def empresas(request):
    nome_filtrar = request.GET.get('nome')
    empresas = Empresa.objects.all()


    if nome_filtrar:
        empresas = empresas.filter(nome__icontains=nome_filtrar)

    return render(request, 'empresa.html', {'empresas': empresas,})

def editar_empresa(request,id):
    empresa = Empresa.objects.get(id=id)
    

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa deletada com sucesso')
    return redirect('/empresas/empresas')

def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    #vagas = Vagas.objects.filter(empresa_id=id)
    #formVagas = FormVagas()
    context={
        'empresa': empresa_unica,
        'empresas': empresas, 
        #'vagas': vagas,
        #'formVagas':formVagas

    }
    return render(request, 'empresa_unica.html', context) 

def vincular_empresa(request):
    if request.method == "POST":
        print("Dados recebidos no POST:", request.POST)
        empresa_id = request.POST.get('empresa_id')
        if empresa_id:
            try:
                empresa = Empresa.objects.get(id=empresa_id)
                empregador = Empregador.objects.get(cpf=request.session['empregador_id'])
                empregador.empresa = empresa
                empregador.save()
                messages.success(request, 'Empresa vinculada com sucesso.')
                return redirect('/vagas/vagas_empregador')  # Altere para a página desejada após a vinculação
            except Empresa.DoesNotExist:
                messages.error(request, 'Empresa não encontrada.')
        else:
            messages.error(request, 'Nenhuma empresa selecionada.')
    return render(request, 'selecionar_empresa.html')


from django.http import JsonResponse

def search_empresas(request):
    empresa = request.GET.get('empresa')
    payload = []
    if empresa:
        empresas_objs = Empresa.objects.filter(nome__icontains=empresa)
        payload = [{'id': empresa_obj.id, 'nome': empresa_obj.nome} for empresa_obj in empresas_objs]
    return JsonResponse({'results': payload})


    
