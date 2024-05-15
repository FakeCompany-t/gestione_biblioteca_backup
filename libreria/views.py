from django.shortcuts import render
from .models import Libro


def home(request):
    libri = Libro.objects.prefetch_related("libroautore_set").all()
    return render(request, 'libreria/home.html', {'libri': libri})
