from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from prestiti.models import Prestito


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Creiamo l'username concatenando il cognome e il nome
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can Log In')      
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if 'remove_picture' in request.POST and request.POST['remove_picture'] == 'true':
            request.user.profile.image = 'profile_default.png'
            request.user.profile.save()
            messages.success(request, 'Il tuo account è stato correttamente modificato!')
            return redirect('profile')

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Il tuo account è stato correttamente modificato!')
            return redirect('profile')
        else:
            messages.error(request, 'Si è verificato un errore nella modifica del tuo account.')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Tabella prestiti
    if request.user.profile.ruolo == 'bibliotecario':
        prestiti = Prestito.objects.all()
    else:
        prestiti = Prestito.objects.filter(user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'prestiti': prestiti
    }

    return render(request, 'users/profile.html', context)


