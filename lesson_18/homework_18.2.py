from urllib.parse import quote
import requests
BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "test_image.jpg"

# POST - завантажуємо зображення на сервер
with open(IMAGE_PATH, "rb") as image:
    response = requests.post(f"{BASE_URL}/upload", files={"image": image})
print("POST /upload:", response.status_code)
print(response.json())
image_url = response.json()["image_url"]
filename = image_url.split("/")[-1]

# GET - отримуємо посилання на файл
response = requests.get(
    f"{BASE_URL}/image/{quote(filename)}",
    headers={"Content-Type": "text"},
)
print("\nGET /image:", response.status_code)
print(response.json())

# DELETE - видаляємо файл із сервера
response = requests.delete(f"{BASE_URL}/delete/{quote(filename)}")
print("\nDELETE /delete:", response.status_code)
print(response.json())
