from flask import Flask, request
from view import View
from meteo import Meteo
from adresse import Adresse

app = Flask(__name__)


@app.route('/')
def home():
    return View.home()


@app.route('/address', methods=['POST'])
def address():
    '''Permet de retourner la page html correspondant à la météo à
    l'adresse demandée
    '''
    adress_number = request.form['num']
    adress_type = request.form['type_voie']
    adress_name = request.form['nom_voie']
    adress_postal = request.form['code_postal']

    print(f"L'adresse est : {adress_number},{adress_type} {adress_name}, {adress_postal}")

    user_adress = Adresse(int(adress_number),
                          str(adress_type),
                          str(adress_name),
                          int(adress_postal))

    meteo = Meteo(user_adress)
    temp, code = meteo.donne_meteo()
    adresse = f"{adress_number}, {adress_type} {adress_name}, {adress_postal}"
    print(f"La température est de {temp}°C.")
    return View.functions[code](adresse, temp)


if __name__ == '__main__':
    app.run(debug=True)
