from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import LibroCreateView, LibroDetailView, LibroDeleteView, AutoreCreateView, CasaEditriceCreateView
from . import views

urlpatterns = [
    path('', views.home, name="libreria-home"),
    path('libro/new/', LibroCreateView.as_view(), name="libro-create"),
    path('libro/<int:pk>/', LibroDetailView.as_view(), name="libro-detail"),
    path('libro/<int:pk>/delete/', LibroDeleteView.as_view(), name="libro-delete"),
    path('autore/new/', AutoreCreateView.as_view(), name="autore-create"),
    path('casa_editrice/new/', CasaEditriceCreateView.as_view(), name="casa_editrice-create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)