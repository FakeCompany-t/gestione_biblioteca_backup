from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Lingua(models.Model):
    lang_code = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.lang_code}"

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
    lingua = models.ForeignKey(Lingua , on_delete=models.PROTECT, default=None)
    isbn = models.IntegerField(null=True, default=0)
    disponibile = models.BooleanField(default=False) 

    def __str__(self):
        return self.title
    
class LibroAutore(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    # Altri campi specifici della relazione
    
    def __str__(self):
        return f"{self.libro.title} - {self.autore.nome} {self.autore.cognome}"
    

