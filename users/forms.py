from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    RUOLO_CHOICES = [
        ('studente', 'Studente'),
        ('docente', 'Docente'),
        ('bibliotecario', 'Bibliotecario'),
        ('segreteria', 'Segreteria'),
        ('gestore_comodato', 'Gestore Comodato d\'Uso'),
    ]
    ruolo = forms.ChoiceField(choices=RUOLO_CHOICES)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user, ruolo=self.cleaned_data['ruolo'])  # Salva il ruolo nel profilo
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']