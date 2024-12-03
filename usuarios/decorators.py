from django.shortcuts import redirect

def login_required_candidato(view_func):
    def wrapper(request, *args, **kwargs):
        if 'candidato_id' not in request.session:
            return redirect('login_candidato')  # Redirecionar para a página de login
        return view_func(request, *args, **kwargs)
    return wrapper

def login_required_empregador(view_func):
    def wrapper(request, *args, **kwargs):
        if 'empregador_id' not in request.session:
            return redirect('login_empregador')  # Redirecionar para a página de login
        return view_func(request, *args, **kwargs)
    return wrapper