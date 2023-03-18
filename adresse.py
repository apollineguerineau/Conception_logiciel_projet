from bulk_geocoding import geocode

class Adresse:
    def __init__(self, numero, type_voie, nom_voie, code_postal):
        self.numero = numero
        self.type_voie = type_voie
        self.nom_voie = nom_voie
        self.code_postal = code_postal

    def donne_latitude_longitude(self) : 
        geocoded = geocode(
        data=[{"numero": self.numero, "type_voie": self.type_voie, "nom_voie": self.nom_voie, "code_postal": self.code_postal}],
        columns=["numero", "type_voie", "nom_voie"],
        citycode="code_postal"
        )
        return([float(geocoded[0]['latitude']), float(geocoded[0]['longitude'])]) 

adresse1=Adresse(3, "rue", "Louis Chouinard", 35170)
print(adresse1.donne_latitude_longitude())