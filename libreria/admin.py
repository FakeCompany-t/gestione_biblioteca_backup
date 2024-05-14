from django.contrib import admin
from .models import Libro, Autore, LibroAutore

class LibroAutoreInline(admin.TabularInline):
    model = LibroAutore

class LibroAdmin(admin.ModelAdmin):
    inlines = [
        LibroAutoreInline,
    ]

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autore)