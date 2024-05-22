from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import PrestitoDeleteView
from . import views
from .views import prestito


urlpatterns = [
    path('profile/<int:pk>/delete/', PrestitoDeleteView.as_view(), name="prestito_delete"),

]
