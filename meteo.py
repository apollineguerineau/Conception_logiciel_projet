import requests


class Meteo:
    def __init__(self, adresse):
        self.adresse = adresse

    def donne_meteo(self):
        latitude, longitude = self.adresse.donne_latitude_longitude()
        r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&current_weather=true')
        response = r.json()['current_weather']
        code = response['weathercode']
        temp = response['temperature']
        return (temp, code)
