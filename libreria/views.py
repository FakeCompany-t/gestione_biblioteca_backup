from django.shortcuts import render

books = [
    {
        'author': 'Dante',
        'title' : 'Divina commedia'
    },


    ]

def home(request):
    context = {
        'books': books,
        'title':'Home'
    }
    return render(request, 'libreria/home.html', context)
