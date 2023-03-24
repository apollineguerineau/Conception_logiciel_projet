from bulk_geocoding import geocode


class Adresse_Exception(Exception):
    '''Permet de gérer l' exception si l'utilisateur rentre une adresse
    incorrecte.
    '''
    def __str__(self):
        return ("L'adresse n'existe pas")


class Adresse:
    '''Classe permettant de gérer la traduction d'adresses en
    latitude/longitude
    '''
    def __init__(self, numero, type_voie, nom_voie, code_postal):
        self.numero = numero
        self.type_voie = type_voie
        self.nom_voie = nom_voie
        self.code_postal = code_postal

    def donne_latitude_longitude(self):
        '''Retourne la latitude et la longitude d'une adresse grâce au
        package python geocode
        '''
        geocoded = geocode(
            data=[
                {"numero": self.numero,
                 "type_voie": self.type_voie,
                 "nom_voie": self.nom_voie,
                 "code_postal": self.code_postal}
                ],
            columns=["numero", "type_voie", "nom_voie"],
            citycode="code_postal"
                )
        if geocoded[0]['result_status'] == 'not-found':
            raise Adresse_Exception()
        latitude = float(geocoded[0]['latitude'])
        longitude = float(geocoded[0]['longitude'])
        return ([latitude, longitude])
