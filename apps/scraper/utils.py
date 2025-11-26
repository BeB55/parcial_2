import requests

def scrape_wikipedia(keyword, limit=10):
    url = "https://es.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "format": "json",
        "srlimit": limit,
    }
    resp = requests.get(url, params=params, timeout=10)
    data = resp.json()

    resultados = []
    for item in data.get("query", {}).get("search", []):
        titulo = item.get("title")
        resumen = item.get("snippet")
        link = f"https://es.wikipedia.org/wiki/{titulo.replace(' ', '_')}"
        resultados.append({"titulo": titulo, "resumen": resumen, "url": link})
    return resultados
