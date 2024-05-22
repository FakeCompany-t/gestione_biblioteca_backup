from django.urls import path,include
from django.conf import settings
from .views import PrestitoDetailView

urlpatterns = [
    path('prestiti/<int:pk>/', PrestitoDetailView.as_view(), name="prestito-detail"),
]