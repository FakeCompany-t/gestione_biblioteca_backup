from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView
from .forms import ConfermaPrestito
from .models import Prestito
from libreria.models import Libro  # Assicurati di importare il modello Libro dalla libreria
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

@login_required
def prestito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        prestito_form = ConfermaPrestito(request.POST)
        if prestito_form.is_valid():
            prestito = Prestito(
                user=request.user,
                libro=libro,
                data_inzio=datetime.now().date(),
                data_fine=(datetime.now() + timedelta(days=30)).date(),
                stato='richiesta'  # Set the initial state
            )
            prestito.save()
            libro.disponibile = 0 
            libro.save()
            messages.success(request, 'La tua richiesta di prestito è stata inviata!')
            return redirect('profile')
    else:
        prestito_form = ConfermaPrestito()
    
    context = {
        'prestito_form': prestito_form,
        'libro': libro
    }
    return render(request, 'profile.html', context)

class PrestitoDetailView(DetailView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice','lingua','isbn','disponibile']
    template_name = 'prestiti/prestito_detail.html'
