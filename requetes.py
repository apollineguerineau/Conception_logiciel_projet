from adresse import Adresse
import requests


class Toobo():
    def __init__(self) -> None:
        self.__HOST = "http://127.0.0.1:8000"

    def adresse_existe(self, adresse):
        payload = {"numero": adresse.numero,
                   "type_voie": adresse.type_voie,
                   "nom_voie": adresse.nom_voie,
                   "code_postal": adresse.code_postal}
        req = requests.get(f"{self.__HOST}/is_adresse", json=payload)
        return req.json()

    def which_weather(self, adresse):
        if self.adresse_existe(adresse):
            payload = {"numero": adresse.numero,
                       "type_voie": adresse.type_voie,
                       "nom_voie": adresse.nom_voie,
                       "code_postal": adresse.code_postal}
            req = requests.get(f"{self.__HOST}/adresse", json=payload)
            return req.json()
        else:
            return ("L'adresse n'existe pas.")


if __name__ == "__main__":
    adresse1 = Adresse(1, "Allée", "du puits de Maran", 33130)
    toobo = Toobo()
    print(toobo.which_weather(adresse1))
