from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from landing.forms import ModificarCampos

def landing_page(request):
    return render(request, 'landing.html')

def registro_page(request):
    if request.method == 'POST':
        form = ModificarCampos(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')  # Redireccionar a la página de inicio después del registro exitoso
    else:
        form = ModificarCampos()
    
    return render(request, 'registro.html', {'form': form})