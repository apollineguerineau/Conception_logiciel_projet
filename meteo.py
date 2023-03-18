import requests
from adresse import Adresse
import constantes

class Meteo:
    def __init__(self, adresse, code):
        self.adresse = adresse
        self.code= code

    def donne_meteo(self):
        latitude, longitude = self.adresse.donne_latitude_longitude()
        r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&current_weather=true')
        response = r.json()['current_weather']
        return(response['weathercode'], response['temperature'], self.code[response['weathercode']]) 


code={0 : "clear sky", 1 : "mainly clear, partly cloudy, and overcast", 2 : "mainly clear, partly cloudy, and overcast", 3 : "mainly clear, partly cloudy, and overcast", 
45: "fog and depositing rime fog", 48:"fog and depositing rime fog", 51:"Drizzle : Light, moderate, and dense intensity", 53:"Drizzle : Light, moderate, and dense intensity",
55:"Drizzle : Light, moderate, and dense intensity", 56 : "Freezing Drizzle: Light and dense intensity", 57 : "Freezing Drizzle: Light and dense intensity",
61:"Rain: slight, moderate and heavy intensity", 63:"Rain: slight, moderate and heavy intensity", 65 : "Rain: slight, moderate and heavy intensity",
66: "freezing rain:light and heavy intensity",67: "freezing rain:light and heavy intensity", 71: "Snow fall : slight, moderate and heavy intensity", 
73: "Snow fall : slight, moderate and heavy intensity", 75: "Snow fall : slight, moderate and heavy intensity", 77 : "snow grains", 
80 : "Rain showers", 81 : "Rain showers",82 : "Rain showers",85 : "Snow showers",86 : "Snow showers", 95 : "thunderstorm", 96:"thunderstorm with slight and heavy hail", 
99:"thunderstorm with slight and heavy hail"}

adresse1=Adresse(3, "Rue", "Louis Chouinard", 35170)
meteo1=Meteo(adresse1, code)
print(meteo1.donne_meteo())

