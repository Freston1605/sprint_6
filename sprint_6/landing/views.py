from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def registro_page(request):
    return render(request, 'registro.html')