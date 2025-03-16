import requests

API_KEY = "write in the ur weathermap api"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{city} için hava durumu: {desc}, sıcaklık: {temp}°C"
    else:
        return "Hava durumu bilgisi alınamadı."
