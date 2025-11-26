import requests
from bs4 import BeautifulSoup

def scrape_python_docs():
    url = "https://www.python.org/doc/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Buscar links dentro de la sección de documentación
    links = soup.select("a")
    resultados = []
    for link in links:
        href = link.get("href")
        texto = link.text.strip()
        if href and texto:
            resultados.append({"texto": texto, "url": href})

    return resultados[:10]  # devolver los primeros 10 resultados
