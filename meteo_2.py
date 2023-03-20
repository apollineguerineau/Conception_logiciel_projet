import requests
from adresse import Adresse
import os
from dotenv import load_dotenv
load_dotenv()

class Meteo:
    def __init__(self, adresse):
        self.adresse = adresse

    def donne_meteo(self):
        codes = os.environ.get("CODE")
        codes = dict(subString.split(":") for subString in codes.split(","))
        return codes
        # latitude, longitude = self.adresse.donne_latitude_longitude()
        # r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&current_weather=true')
        # response = r.json()['current_weather']
        # code = response['weathercode']
        # return(code, response['temperature'], codes[code]) 


adresse1=Adresse(16, "Rue", "de la République", 57320)
meteo1=Meteo(adresse1)
print(meteo1.donne_meteo())

