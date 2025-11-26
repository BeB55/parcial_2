import requests

WIKI_API_URL = "https://es.wikipedia.org/w/api.php"
WIKI_PAGE_URL = "https://es.wikipedia.org/wiki/"

def scrape_palabra(palabra: str, limite: int = 10):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": palabra,
        "format": "json",
        "srlimit": limite,
    }
    resp = requests.get(WIKI_API_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    resultados = []
    for item in data.get("query", {}).get("search", []):
        titulo = item.get("title", "")
        resumen = item.get("snippet", "")
        url = WIKI_PAGE_URL + titulo.replace(" ", "_")
        resultados.append({
            "titulo": titulo,
            "url": url,
            "resumen": resumen,
        })
    return resultados
