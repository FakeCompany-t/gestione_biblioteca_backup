from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"
    

class Casa_editrice(models.Model):
    nome = models.CharField(max_length=100)
    nazionalita = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Libro(models.Model):
    copertina = models.ImageField(default='default.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    data_publication = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(datetime.now().year)])
    casa_editrice = models.ForeignKey(Casa_editrice , on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title
    
class LibroAutore(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    # Altri campi specifici della relazione
    
    def __str__(self):
        return f"{self.libro.title} - {self.autore.nome} {self.autore.cognome}"
    

