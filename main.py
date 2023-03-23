from adresse import *
from meteo import Meteo
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


app = FastAPI()


class AdresseCreation(BaseModel):
    # pylint: disable=too-few-public-methods
    """classe PartieCreation pour la transmission d'informations

    Parameters
    ----------
    BaseModel : BaseModel
        classe mère
    """
    numero: int
    type_voie: str
    nom_voie: str
    code_postal: int


@app.get("/is_adresse")
async def get_meteo(adresse: AdresseCreation):
    numero = adresse.numero
    type_voie = adresse.type_voie
    nom_voie = adresse.nom_voie
    code_postal = adresse.code_postal
    adresse = Adresse(numero, type_voie, nom_voie, code_postal)
    meteo = Meteo(adresse)
    try :
        adresse.donne_latitude_longitude()
    except Adresse_Exception :
        return (False)
    return(True)

@app.get("/adresse")
async def get_meteo(adresse: AdresseCreation):
    numero = adresse.numero
    type_voie = adresse.type_voie
    nom_voie = adresse.nom_voie
    code_postal = adresse.code_postal
    adresse = Adresse(numero, type_voie, nom_voie, code_postal)
    meteo = Meteo(adresse)
    return (meteo.donne_meteo())

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
