from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    RUOLO_CHOICES = [
        ('studente', 'Studente'),
        ('docente', 'Docente'),
        ('bibliotecario', 'Bibliotecario'),
        ('segreteria', 'Segreteria'),
        ('gestore_comodato', 'Gestore Comodato d\'Uso'),
        ('amministratore', 'amministratore'),

    ]
    ruolo = models.CharField(max_length=20, choices=RUOLO_CHOICES)

