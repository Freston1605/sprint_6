from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, EmailAuthenticationForm


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

def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la página después del inicio de sesión exitoso
                return redirect('home')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige a la página principal después del cierre de sesión

def home(request):
    return render(request, 'home.html')