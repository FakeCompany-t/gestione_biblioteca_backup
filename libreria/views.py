from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Libro, Autore, LibroAutore


def home(request):
    libri = Libro.objects.prefetch_related("libroautore_set__autore").all()
    return render(request, 'libreria/home.html', {'libri': libri})
class LibroCreateView(CreateView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice']

    def form_valid(self, form):
        # Assegna l'utente corrente come creatore del libro
        form.instance.creatore = self.request.user
        # Salva il libro
        self.object = form.save()
        # Ottieni gli autori selezionati dalla form
        autori_selezionati = self.request.POST.getlist('autori')
        # Associa gli autori al libro
        for autore_id in autori_selezionati:
            libro_autore = LibroAutore.objects.create(libro=self.object, autore_id=autore_id)
            libro_autore.save()
        messages.success(self.request, 'Libro creato con successo!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libreria-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autori'] = Autore.objects.all()  # Aggiungi gli autori al contesto
        return context
class LibroDetailView(DetailView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice']

class LibroDeleteView(DeleteView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice']
    success_url = '/'
