import requests
from bs4 import BeautifulSoup

def scrape_python_docs(keyword):
    url = "https://docs.python.org/3/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    resultados = []
    # Buscar links que contengan la palabra clave
    for link in soup.select("a"):
        href = link.get("href")
        texto = link.text.strip()
        if href and texto and keyword.lower() in texto.lower():
            # Convertir links relativos en absolutos
            if href.startswith("http"):
                full_url = href
            else:
                full_url = f"https://docs.python.org/3/{href}"
            resultados.append({"titulo": texto, "url": full_url})

    return resultados[:10]
