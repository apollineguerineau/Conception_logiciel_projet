from adresse import Adresse
import requests


class Toobo():
    """gère
    """
    def __init__(self) -> None:
        self.__HOST = "http://127.0.0.1:8000"

    def which_weather(self, adresse):
        payload = {"numero": adresse.numero,
                   "type_voie": adresse.type_voie,
                   "nom_voie": adresse.nom_voie,
                   "code_postal": adresse.code_postal}
        req = requests.get(f"{self.__HOST}/adresse", json=payload)
        return req.json()


if __name__ == "__main__":
    adresse1 = Adresse(10, "Place", "Paul et Jean-Paul Avisseau", 33300)
    toobo = Toobo()
    print(toobo.which_weather(adresse1))
