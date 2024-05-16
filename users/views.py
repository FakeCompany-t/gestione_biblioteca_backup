from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfilePictureForm

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


def profile(request):
    
    return render(request, 'users/profile.html') 

def change_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvataggio della nuova immagine del profilo nel profilo dell'utente
            request.user.profile.image = form.cleaned_data['picture']
            request.user.profile.save()
            return redirect('profile')  # Redirect alla pagina del profilo dopo aver cambiato l'immagine
    else:
        form = ProfilePictureForm()
    
    return render(request, 'libreria/change_profile_picture.html', {'form': form})
