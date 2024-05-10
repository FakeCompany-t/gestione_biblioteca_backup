from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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


