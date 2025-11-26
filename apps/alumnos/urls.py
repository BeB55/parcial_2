from django.urls import path
from .views import enviar_pdf
from .views import scraper_view

urlpatterns = [
    path("enviar_pdf/<int:alumno_id>/", enviar_pdf, name="enviar_pdf"),
    path("scraper/", scraper_view, name="scraper"),
]
