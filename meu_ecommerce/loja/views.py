from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def dashboard(request):
    # Exibe dashboard diferente para cliente ou vendedor
    if hasattr(request.user, 'tipo'):
        if request.user.tipo == 'cliente':
            return render(request, 'dashboard_cliente.html')
        elif request.user.tipo == 'vendedor':
            return render(request, 'dashboard_vendedor.html')
    # Caso o usuario não tenha 'tipo', redireciona para main
    return redirect('main')


def index(request):
    # Página inicial publica
    return render(request, 'index.html')


def signup(request):
    # Cadastro de usuario
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # loga automaticamente após cadastro
            return redirect('dashboard')  # envia para dashboard
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
