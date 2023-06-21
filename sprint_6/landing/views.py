from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def landing_page(request):
    return render(request, 'landing.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # Guarda al usuario en la base de datos
            # Realiza las acciones adicionales que desees, 
            # como iniciar sesión automáticamente, 
            # redirigir a una página de inicio, etc.
            return redirect('landing_page') #Redirigiendo al inicio
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
