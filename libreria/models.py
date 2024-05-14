from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Libro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    data_publication = models.DateField(default=timezone.now)
    autori = models.ManyToManyField(Autore, through= "LibroAutore")

    def __str__(self):
        return self.title
    
class LibroAutore(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    # Altri campi specifici della relazione
    # porco dio
    
    def __str__(self):
        return f"{self.libro.title} - {self.autore.nome} {self.autore.cognome}"