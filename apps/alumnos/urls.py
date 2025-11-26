from django.urls import path
from .views import enviar_pdf

urlpatterns = [
    path("enviar_pdf/<int:alumno_id>/", enviar_pdf, name="enviar_pdf"),
]
