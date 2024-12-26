from django.shortcuts import render

def home(request):
    return render(request, 'nome_do_app/home.html')
