from django.shortcuts import render
from django.core.mail import EmailMessage
import os
from .forms import ScraperForm
from .utils import scrape_wikipedia

def scraper_view(request):
    resultados = []
    form = ScraperForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        palabra = form.cleaned_data["palabra"]
        enviar_correo = form.cleaned_data["enviar_correo"]

        resultados = scrape_wikipedia(palabra)

        if enviar_correo and resultados:
            cuerpo = f"Resultados de búsqueda para: {palabra}\n\n"
            for r in resultados:
                cuerpo += f"- {r['titulo']}: {r['url']}\n"

            email = EmailMessage(
                subject=f"Recursos educativos: {palabra}",
                body=cuerpo,
                from_email=os.environ.get("DEFAULT_FROM_EMAIL"),
                to=[request.user.email],
            )
            email.send()

    return render(request, "scraper.html", {"form": form, "resultados": resultados})
