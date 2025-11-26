import requests
from bs4 import BeautifulSoup

def scrape_keyword(keyword):
    url = f"https://www.wikipedia.org/search-redirect.php?search={keyword}&language=es"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    resultados = []
    for link in soup.select("a"):
        href = link.get("href")
        texto = link.text.strip()
        if href and texto:
            resultados.append({"texto": texto, "url": href})

    return resultados[:10]  # devolver los primeros 10
