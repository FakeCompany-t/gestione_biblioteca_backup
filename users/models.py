from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    RUOLO_CHOICES = [
        ('studente', 'Studente'),
        ('docente', 'Docente'),
        ('bibliotecario', 'Bibliotecario'),
        ('segreteria', 'Segreteria'),
        ('gestore_comodato', 'Gestore Comodato d\'Uso'),
        ('amministratore', 'Amministratore'),

    ]
    ruolo = models.CharField(max_length=20, choices=RUOLO_CHOICES)
    image = models.ImageField(default='profile_default.png', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user}"


