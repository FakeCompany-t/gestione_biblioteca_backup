from django.contrib import admin
from .models import Libro, Autore, LibroAutore , Casa_editrice , Lingua ,Tag , LibroTag

admin.site.register(Libro)
admin.site.register(Tag)
admin.site.register(Autore)
admin.site.register(Casa_editrice)
admin.site.register(LibroTag)
admin.site.register(LibroAutore)
admin.site.register(Lingua)
