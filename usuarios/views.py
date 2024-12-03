from django.shortcuts import render, redirect, get_object_or_404
from .decorators import login_required_candidato, login_required_empregador
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages import constants
from .forms import CandidatoForms, EmpregadorForms, PerfilCandidatoForms, EditarCandidatoForms, EditarEmpregadorForms
from .models import Candidato, Empregador
from empresa.models import Empresa
from vagas.models import Vagas

def home(request):
    vagas = Vagas.objects.all()
    empresas = Empresa.objects.all()

    context={
        'vagas':vagas,
        'empresas':empresas
    }
    return render(request, 'home.html')

def registro_candidato(request):
    if request.method == 'POST':
        form = CandidatoForms(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login_candidato')
        else:
            print(form.errors)  # Adicionar esta linha para verificar se há erros no formulário
    else:
        form = CandidatoForms()
    return render(request, 'registro_candidato.html', {'form': form})

def registro_empregador(request):
    if request.method == 'POST':
        form = EmpregadorForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_empregador')
        else:
            print(form.errors)
    else:
        form = EmpregadorForms()
    return render(request, 'registro_empregador.html', {'form': form})

def login_candidato(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        try:
            candidato = Candidato.objects.get(email=email)
            if candidato.check_password(senha):
                # Armazenar informações do usuário na sessão
                request.session['candidato_id'] = candidato.pk
                request.session['candidato_nome'] = candidato.nome
                if not candidato.area_atuacao or not candidato.curriculo or not candidato.imagem:
                    # Redireciona para completar o perfil
                    return redirect('completar_perfil')

                return redirect('/vagas/vagas_candidato')
            else:
                messages.error(request, 'Senha incorreta')
        except Candidato.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')
    
    return render(request, 'login_candidato.html')

def login_empregador(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        try:
            empregador = Empregador.objects.get(email=email)
            if empregador.check_password(senha):
                # Armazenar informações do usuário na sessão
                request.session['empregador_id'] = empregador.pk    
                request.session['empregador_nome'] = empregador.nome
                print(empregador.pk)
                if not empregador.empresa:
                    return redirect('empresas/vincular_empresa')
                return redirect('/vagas/vagas_empregador')
            else:
                messages.error(request, 'Senha incorreta')
        except Empregador.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')
    
    return render(request, 'login_empregador.html')

def completar_perfil(request):
    candidato = Candidato.objects.get(pk=request.session['candidato_id'])
    
    if request.method == 'POST':
        form = PerfilCandidatoForms(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('/vagas/vagas_candidato')
    else:
        form = PerfilCandidatoForms(instance=candidato)

    return render(request, 'completar_perfil.html', {'form': form})

def perfil_candidato(request):
    candidato = request.session['candidato_id']
    perfil = get_object_or_404(Candidato, pk=candidato)
    if not perfil.area_atuacao or not perfil.curriculo or not perfil.imagem:
        return redirect('completar_perfil')
    context = {
        'perfil': perfil
    }
    print(perfil.curriculo.url)
    return render(request, 'perfil_candidato.html', context)

def perfil_empregador(request):
    empregador = request.session['empregador_id']
    perfil = get_object_or_404(Empregador, pk=empregador)
    context = {
        'perfil': perfil
    }
    return render(request, 'perfil_empregador.html', context)

def editar_candidato(request):
    candidato = request.session['candidato_id']
    candidato = get_object_or_404(Candidato, pk=candidato)
    if request.method == 'POST':
        form = EditarCandidatoForms(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('perfil_candidato')
        else:
            print(form.errors)
    else:
        form = EditarCandidatoForms(instance=candidato)
    context={
        'form': form,
        'candidato': candidato,
    }
    return render(request, 'editar_candidato.html', context)

def editar_empregador(request):
    empregador = request.session['empregador_id']
    empregador = get_object_or_404(Empregador, pk=empregador)
    if request.method == 'POST':
        form = EditarEmpregadorForms(request.POST, request.FILES, instance=empregador)
        if form.is_valid():
            form.save()
            return redirect('perfil_empregador')
        else:
            print(form.errors)
    else:
        form = EditarEmpregadorForms(instance=empregador)
    context={
        'form': form,
        'empregador': empregador,
    }
    return render(request, 'editar_empregador.html', context)

def logout_candidato(request):
    if 'candidato_id' in request.session:
        del request.session['candidato_id']
        del request.session['candidato_nome']
    return redirect('/login_candidato')

def logout_empregador(request):
    if 'empregador_id' in request.session:
        del request.session['empregador_id']
        del request.session['empregador_nome']
    return redirect('/login_empregador')



