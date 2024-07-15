from django.shortcuts import render

def empanadas(request):
    return render(request, 'empanadas.html')