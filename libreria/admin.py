from django.contrib import admin
from .models import Libro, Autore, LibroAutore , Casa_editrice , Lingua

admin.site.register(Libro)
admin.site.register(Autore)
admin.site.register(Casa_editrice)
admin.site.register(LibroAutore)
admin.site.register(Lingua)
