from flask import Flask, request, render_template
from view import View
from meteo import Meteo
from adresse import *

app = Flask(__name__)

@app.route('/')
def home():
    return View.home()

@app.route('/address', methods=['POST'])
def address():
    adress_number = request.form['num']
    adress_type = request.form['type_voie']
    adress_name = request.form['nom_voie']
    adress_postal = request.form['code_postal']
    print(adress_number, adress_type, adress_name, adress_postal)
    user_adress = Adresse(int(adress_number), str(adress_type), str(adress_name), int(adress_postal))
    print(f"L'adresse est : {adress_number}, {adress_type} {adress_name}, {adress_postal}")
    meteo = Meteo(user_adress)
    print(meteo.donne_meteo())
    #temp, code = Meteo.donne_meteo()
    return render_template("snow_grains.html")
    # return Vie.drizzle()
    #     return f"""<head><title>Meteo</title>
    #             <meta charset=utf-8> </head>
    #             <body>
    #                 <h3>Il grêle au {user_address}, votre jardin pourrait donc ressembler à ceci :</h3>
    #                 <img
    #                 src="data:thunderstorm/png;base64, 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"
    #                 width="400px">
    #             </body>"""
    # # Utilisez user_address pour générer le contenu HTML de votre choix
    # return f"<h1>Voici le contenu généré pour l'adresse : {user_address}</h1>"

if __name__ == '__main__':
    app.run(debug=True)