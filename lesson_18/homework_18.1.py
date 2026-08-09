import requests

BASE_URL = "https://images-api.nasa.gov"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20,
}

response = requests.get(f"{BASE_URL}/search", params=search_params)
items = response.json()["collection"]["items"]

nasa_ids = [item["data"][0]["nasa_id"] for item in items[:2]]

print("Знайдені nasa_id:", nasa_ids)
for number, nasa_id in enumerate(nasa_ids, start=1):
    asset_response = requests.get(f"{BASE_URL}/asset/{nasa_id}")
    files = [f["href"] for f in asset_response.json()["collection"]["items"]]
    
    jpg_url = next(url for url in files if url.lower().endswith(".jpg"))
    
    image = requests.get(jpg_url)
    filename = f"mars_photo{number}.jpg"
    with open(filename, "wb") as f:
        f.write(image.content)
        
    print(f"Збережено {filename} <- {jpg_url}")
