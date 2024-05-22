from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from libreria.models import Libro
from django.contrib.auth.models import User

def durata_prestito():
    return datetime.now()+timedelta(days = 30)

class Prestito(models.Model):
    libro = models.ForeignKey(Libro , on_delete=models.PROTECT, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inzio = models.DateField(default=timezone.now)
    data_fine = models.DateField(default=durata_prestito) 
    STATO_CHOICES = [
        ('richiesta', 'Richiesta'),
        ('in corso', 'In corso'),
        ('riconsegna', 'Riconsegna'),
        ('chiuso', 'Chiuso'),
        ]
    stato = models.CharField(max_length=20, choices=STATO_CHOICES)


    def __str__(self):
        return f"{self.libro} {self.user} {self.data_fine}"
