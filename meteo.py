import requests


class Meteo:
    def __init__(self, adresse):
        self.adresse = adresse

    def donne_meteo(self):
        latitude, longitude = self.adresse.donne_latitude_longitude()
        r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&current_weather=true')
        response = r.json()['current_weather']
        code = response['weathercode']
        return (response['temperature'], codes[code])


codes = {0: "clear sky", 1: "mainly clear, partly cloudy, and overcast", 2: "mainly clear, partly cloudy, and overcast", 3: "mainly clear, partly cloudy, and overcast",
         45: "fog and depositing rime fog", 48: "fog and depositing rime fog", 51: "Drizzle : Light, moderate, and dense intensity", 53: "Drizzle : Light, moderate, and dense intensity",
         55: "Drizzle : Light, moderate, and dense intensity", 56: "Freezing Drizzle: Light and dense intensity", 57: "Freezing Drizzle: Light and dense intensity",
         61: "Rain: slight, moderate and heavy intensity", 63: "Rain: slight, moderate and heavy intensity", 65: "Rain: slight, moderate and heavy intensity",
         66: "freezing rain:light and heavy intensity", 67: "freezing rain:light and heavy intensity", 71: "Snow fall : slight, moderate and heavy intensity",
         73: "Snow fall : slight, moderate and heavy intensity", 75: "Snow fall : slight, moderate and heavy intensity", 77: "snow grains",
         80: "Rain showers", 81: "Rain showers", 82: "Rain showers", 85: "Snow showers", 86: "Snow showers", 95: "thunderstorm", 96: "thunderstorm with slight and heavy hail",
         99: "thunderstorm with slight and heavy hail"}
