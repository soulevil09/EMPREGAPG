from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.http import Http404
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from .models import Vagas
from empresa.models import Empresa
from usuarios.models import Empregador, Candidato
from .forms import FormVagas
from usuarios.decorators import *
from seletive.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

def nova_vaga(request):
    if request.method == 'POST':
        formVagas = FormVagas(request.POST, request.FILES)
        if formVagas.is_valid():
            formVagas.save()
            vagas = Vagas.objects.get(titulo=request.POST.get('titulo'))
            empregador = Empregador.objects.get(cpf=request.session['empregador_id'])
            vagas.empresa, vagas.empregador = empregador.empresa, empregador
            # vagas.empregador = empregador 
            vagas.save()
            messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso')
            return redirect('/vagas/vagas_empregador')
        else:
            # Em caso de formulário inválido, renderize a página com os erros
            messages.add_message(request, constants.ERROR, 'Erro ao criar a vaga. Verifique os dados e tente novamente.')
            return render(request, 'empresa_unica.html', {'formVagas': formVagas})
    else:
        formVagas = FormVagas()
        context={
            'formVagas':formVagas
        }
    
    return render(request, 'nova_vaga.html', context)


@login_required_candidato
def vagas_candidato(request):
    vagas = Vagas.objects.all()
    empresas = Empresa.objects.all()

    context={
        'vagas':vagas,
        'empresas':empresas
    }
    return render(request, 'vagas_candidato.html', context)

@login_required_empregador
def vagas_empregador(request):
    empresas = Empresa.objects.all()
    empregador = Empregador.objects.get(cpf=request.session['empregador_id'])
    vagas = Vagas.objects.filter(empregador=empregador) 

    context={
        'vagas':vagas,
        'empresas':empresas
    }
    return render(request, 'vagas_empregador.html', context)


def vaga_unica(request, id):
    vaga_detalhe = get_object_or_404(Vagas, id=id)
    context={
        'vaga': vaga_detalhe,
    }
    return render(request, 'detalhe_vaga.html', context) 


def editar_vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    if request.method == "POST":
        form = FormVagas(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('vagas_empregador')
    else:
        form = FormVagas(instance=vaga)
    context={
        'form':form,
        'vaga':vaga,
    }
    return render(request, 'editar_vaga.html', context)

def excluir_vaga(request, id):
    vaga = Vagas.objects.get(id=id)
    vaga.delete()
    messages.add_message(request, constants.SUCCESS, 'Vaga deletada com sucesso')
    return redirect('/vagas/vagas_empregador')

def candidatar_vaga(request, vaga_id):
    if request.method == 'POST':
        # Obter a vaga e o candidato logado
        vaga = get_object_or_404(Vagas, id=vaga_id)
        candidato = get_object_or_404(Candidato, pk=request.session['candidato_id'])  

        if not candidato.curriculo:
            messages.error(request, "Você precisa anexar um currículo ao seu perfil antes de se candidatar.")
            return redirect('detalhes_vaga', vaga_id=vaga_id)
        
        empregador = vaga.empregador
        if vaga.empregador is None:
            messages.error(request, 'Esta vaga nao esta associada a nenhum empregador.')
            return redirect('vagas_candidato')

        # Enviar e-mail
        try:
            subject = f"Candidatura à vaga: {vaga.titulo}"
            message = f"Olá {vaga.empresa.nome},\n\n{candidato.nome} está se candidatando à sua vaga.\n\nConfira o currículo em anexo."
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=EMAIL_HOST_USER,
                to=[empregador.email],
            )
            # Adicionar o currículo como anexo
            email.attach_file(candidato.curriculo.path)
            email.send()

            messages.success(request, "Sua candidatura foi enviada com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao enviar a candidatura: {e}")

        redirect_url = reverse('vagas_candidato')
        print(redirect_url)  # Exibirá a URL gerada no terminal
        return render(request, 'carregando_candidatura.html', {'redirect_url': redirect_url})

def carregando_candidatura(request):
    return render(request, 'carregando_candidatura.html')
     
