from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import LibroCreateView, LibroDetailView, LibroDeleteView
from . import views
from .views import cerca_autori

urlpatterns = [
    path('', views.home, name="libreria-home"),
    path('libro/new/', LibroCreateView.as_view(), name="libro-create"),
    path('libro/<int:pk>/', LibroDetailView.as_view(), name="libro-detail"),
    path('libro/<int:pk>/delete/', LibroDeleteView.as_view(), name="libro-delete"),
     path('api/cerca_autori', cerca_autori, name='cerca_autori'),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)