import httpx

SHIKIMORI_URL = "https://shikimori.io/api/animes"

HEADERS = {
    "User-Agent": "MyShikimoriBot/1.0"
}

async def search_anime(query: str):
    """
    Ищет аниме по названию и возвращает tuple: (название, ссылка_на_сайт)
    """
    params = {
        "search": query,
        "limit": 1  
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(SHIKIMORI_URL, params=params, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                if data:
                    anime = data[0]
                    title = anime.get("russian") or anime.get("name")
                    anime_url = f"https://shikimori.io{anime['url']}"
                    return title, anime_url
        except Exception as e:
            print(f"Ошибка при запросе к API: {e}")
            
    return None, None