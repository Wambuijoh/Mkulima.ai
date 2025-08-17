import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        return {
            "description": desc,
            "temperature": temp,
            "humidity": humidity
        }
    else:
        return {"error": "Weather data not available"}