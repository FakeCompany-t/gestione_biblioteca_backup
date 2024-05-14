from django.shortcuts import render
from .models import Libro


def home(request):
    libri = Libro.objects.prefetch_related("autori").all()
    return render(request, 'libreria/home.html', {'libri':libri})

