from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import os
from .forms import ScraperForm
from .utils import scrape_keyword

@login_required
def scraper_view(request):
    resultados = []
    if request.method == "POST":
        form = ScraperForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            resultados = scrape_keyword(keyword)

            # Enviar por correo
            cuerpo = "Resultados del scraping:\n\n"
            for r in resultados:
                cuerpo += f"- {r['texto']}: {r['url']}\n"

            email = EmailMessage(
                subject=f"Scraping educativo: {keyword}",
                body=cuerpo,
                from_email=os.environ.get("DEFAULT_FROM_EMAIL"),
                to=[request.user.email],
            )
            email.send()
    else:
        form = ScraperForm()

    return render(request, "scraper.html", {"form": form, "resultados": resultados})
