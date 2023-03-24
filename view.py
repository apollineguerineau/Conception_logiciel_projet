class View:
    def __init__(self):
        return

    def home():
        return '''
          <head>
            <title>La météo en instantanée avec Toobo</title>
        </head>
        <h1>La météo en instantanée avec Toobo</h1>
        <body>
            <form method="POST" action="/address">
            <label for="num">Entrez votre numéro de rue:</label>
            <input
                type="text"
                id="num"
                name="num"
                placeholder="ex : 51"
                size="30"><br>
            <label for="type_voie">Entrez le type de la voie:</label>
            <input
                type="text"
                id="type_voie"
                name="type_voie"
                placeholder="ex : Rue"
                size="30"><br>
            <label for="nom_voie">Entrez le nom de la voie:</label>
            <input
                type="text"
                id="nom_voie"
                name="nom_voie"
                placeholder="ex : Blaise Pascal"
                size="30"><br>
            <label for="code_postal">Entrez le code INSEE de la commune:</label>
            <input
                type="text"
                id="code_postal"
                name="code_postal"
                placeholder="ex : 35047"
                size="30"><br><br>
            <input type="submit" value="Valider"> <br> <br>
            <img src="/static/toobo-bonobo.gif" width="600px">
            </form>
        </body>
    '''

    def clear_sky(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Il fait beau, il fait chaud, le ciel est totalement dégagé au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/clear_sky.gif" width="400px" height="300px">
            </body>"""


    def mainly_clear(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Il fait beau temps, le ciel est partiellement dégagé au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/mainly_clear.gif" width="400px">
            </body>"""

    def fog(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Il fait un temps de genouille (t'as compris, f(r)og) au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/fog.gif" width="400px">
            </body>"""

    def drizzle(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3> Il bruine au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/drizzle.gif" width="400px">
            </body>"""

    def freezing_drizzle(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Prenez garde, il y a de la bruine verglacante au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/freezing.gif" width="400px">
            </body>"""

    def rain(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3> Ca pleut, ça mouille, c'est la fête à la grenouille au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/rain.gif" width="400px">
            </body>"""

    def freezing_rain(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Attention en sortant, il y a des pluies verglaçantes au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/freezing.gif" width="400px">
            </body>"""

    def snow_fall(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3> C'est l'heure des bonhommes de neige au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/snow_fall.gif" width="400px">
            </body>"""

    def snow_grains(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Tous aux abris ! Il grêle au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/snow_grains.gif" width="400px">
            </body>"""

    def rain_shower(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Rain shower au {adresse}, pour les radins, c'est le moment d'en profiter
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/rain_shower.gif" width="400px">
            </body>"""

    def snow_shower(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Sortez les luges, averses de neige au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/snow_shower.gif" width="400px">
            </body>"""

    def thunderstorm(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3> Orage, ô désespoir au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="/static/thunderstrom.gif" width="400px">
            </body>"""

    def thunderstorm_hail(adresse, temp):
        return f"""<head><title>Meteo</title>
                <meta charset=utf-8> </head>
                <body>
                    <h3>Quoi que vous ayez à faire, restez chez vous,
                     c'est la tempête de grêles au {adresse},
                     et la température est de {temp}°C.</h3>
                    <img
                    src="/static/thunderstorm_hail.gif"
                    width="400px">
                </body>"""

    functions = {
    0: clear_sky,
    1: mainly_clear,
    2: mainly_clear,
    3: mainly_clear,
    45: fog,
    48: fog,
    51: drizzle,
    53: drizzle,
    55: drizzle,
    56: freezing_drizzle,
    57: freezing_drizzle,
    61: rain,
    63: rain,
    65: rain,
    66: freezing_rain,
    67: freezing_rain,
    71: snow_fall,
    73: snow_fall,
    75: snow_fall,
    77: snow_grains,
    80: rain_shower,
    81: rain_shower,
    82: rain_shower,
    85: snow_shower,
    86: snow_shower,
    95: thunderstorm,
    96: thunderstorm_hail,
    99: thunderstorm_hail
        }
