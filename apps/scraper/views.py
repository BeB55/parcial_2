from django.shortcuts import render
from django.core.mail import send_mail
import os
from .utils import scrape_python_docs

def scraper_view(request):
    results = []
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        results = scrape_python_docs(keyword)

        # Enviar por correo
        cuerpo = "Resultados del scraping:\n\n"
        for r in results:
            cuerpo += f"- {r['titulo']}: {r['url']}\n"

        send_mail(
            subject=f"Resultados del scraping: {keyword}",
            message=cuerpo,
            from_email=os.environ.get("DEFAULT_FROM_EMAIL"),
            recipient_list=[request.user.email],
        )

    return render(request, "scraper.html", {"results": results})
