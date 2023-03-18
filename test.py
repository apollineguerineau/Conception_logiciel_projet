import requests
latitude = 48.84
longitude = 2.29
r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weathercode&current_weather=true')
response = r.json()['current_weather']
codes={0 : "clear sky", 1 : "mainly clear, partly cloudy, and overcast", 2 : "mainly clear, partly cloudy, and overcast", 3 : "mainly clear, partly cloudy, and overcast", 
45: "fog and depositing rime fog", 48:"fog and depositing rime fog", 51:"Drizzle : Light, moderate, and dense intensity", 53:"Drizzle : Light, moderate, and dense intensity",
55:"Drizzle : Light, moderate, and dense intensity", 56 : "Freezing Drizzle: Light and dense intensity", 57 : "Freezing Drizzle: Light and dense intensity",
61:"Rain: slight, moderate and heavy intensity", 63:"Rain: slight, moderate and heavy intensity", 65 : "Rain: slight, moderate and heavy intensity",
66: "freezing rain:light and heavy intensity",67: "freezing rain:light and heavy intensity", 71: "Snow fall : slight, moderate and heavy intensity", 
73: "Snow fall : slight, moderate and heavy intensity", 75: "Snow fall : slight, moderate and heavy intensity", 77 : "snow grains", 
80 : "Rain showers", 81 : "Rain showers",82 : "Rain showers",85 : "Snow showers",86 : "Snow showers", 95 : "thunderstorm", 96:"thunderstorm with slight and heavy hail", 
99:"thunderstorm with slight and heavy hail"}

print(response['weathercode'])
print(response['temperature'])
print(codes[response['weathercode']])

from bulk_geocoding import geocode

adresses = [
  {"numero": "3", "type_voie": "rue", "nom_voie": "Louis Chouinard", "numero_insee": "35170"}
]

geocoded = geocode(
  data=adresses,
  columns=["numero", "type_voie", "nom_voie"],
  citycode="numero_insee"
)

print(geocoded[0]['latitude'], geocoded[0]['longitude'])