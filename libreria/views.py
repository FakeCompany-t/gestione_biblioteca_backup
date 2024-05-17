from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Libro, Autore, LibroAutore,Tag,LibroTag, Casa_editrice,Lingua
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    libri = Libro.objects.prefetch_related("libroautore_set__autore").all()
    return render(request, 'libreria/home.html', {'libri': libri})



class LibroCreateView(CreateView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice','lingua','isbn']

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

        tag_selezionati = self.request.POST.getlist('tags')  
        for tag_id in tag_selezionati:
            libro_tag = LibroTag.objects.create(libro=self.object, tag_id=tag_id)
            libro_tag.save()
        messages.success(self.request, 'Libro creato con successo!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libreria-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autori'] = Autore.objects.all()  # Aggiungi gli autori al contesto
        context['tags'] = Tag.objects.all()  # Aggiungi i tag al contesto
        context['case_editrici'] = Casa_editrice.objects.all()
        context['lingue'] = Lingua.objects.all()
        return context
class LibroDetailView(DetailView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice','lingua','isbn','disponibile']
    template_name = 'libreria/libro_detail.html'

class LibroDeleteView(DeleteView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice','lingua','isbn','disponibile']
    success_url = '/libreria/'

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['copertina', 'title', 'description', 'data_publication', 'casa_editrice', 'lingua', 'isbn', 'disponibile']

    def form_valid(self, form):
        form.instance.creatore = self.request.user
        self.object = form.save()

        # Aggiunta o rimozione degli autori associati al libro
        autori_selezionati = self.request.POST.getlist('autori')
        LibroAutore.objects.filter(libro=self.object).delete()  # Rimuovi tutte le relazioni libro-autore attuali
        for autore_id in autori_selezionati:
            libro_autore = LibroAutore.objects.create(libro=self.object, autore_id=autore_id)

        # Aggiunta o rimozione dei tag associati al libro
        tag_selezionati = self.request.POST.getlist('tags')
        LibroTag.objects.filter(libro=self.object).delete()  # Rimuovi tutte le relazioni libro-tag attuali
        for tag_id in tag_selezionati:
            libro_tag = LibroTag.objects.create(libro=self.object, tag_id=tag_id)

        messages.success(self.request, 'Libro aggiornato con successo!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libro-detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        # Preseleziona gli autori già associati al libro
        initial['autori'] = [libro_autore.autore.id for libro_autore in LibroAutore.objects.filter(libro=self.object)]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autori'] = Autore.objects.all()
        context['tags'] = Tag.objects.all()
        context['case_editrici'] = Casa_editrice.objects.all()
        context['lingue'] = Lingua.objects.all()
        return context



def cerca_autori(request):
    query = request.GET.get('query', '')
    autori = Autore.objects.filter(nome__icontains=query) | Autore.objects.filter(cognome__icontains=query)
    data = [{'pk': autore.pk, 'nome': autore.nome, 'cognome': autore.cognome} for autore in autori]
    return JsonResponse(data, safe=False)
    success_url = '/'

class AutoreCreateView(CreateView):
    model = Autore
    fields = ['nome', 'cognome']

    def get_success_url(self):
        return reverse_lazy('libreria-home')

class CasaEditriceCreateView(CreateView):
    model = Casa_editrice
    fields = ['nome', 'nazionalita']

    def get_success_url(self):
        return reverse_lazy('libreria-home')
    
def landing_page(request):
    return render(request,'libreria/landing_page.html')

def contact(request):
    return render(request,'libreria/contact.html')
