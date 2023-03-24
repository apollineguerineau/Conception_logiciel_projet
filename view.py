class View:
    def __init__(self, adresse, temp):
        self.adresse = adresse
        self.temp = temp

    def home():
        return '''
          <head>
            <title>La meteo en instantanee</title>
        </head>
        <h1>La meteo en instantanee</h1>
        <body>
            <form method="POST" action="/address">
            <label for="address">Entrez votre adresse:</label>
            <input
                type="text"
                id="address"
                name="address"
                placeholder="ex : 3, Rue de la Liberté, 35000"
                size="30">
            <input type="submit" value="Valider">
            </form>
        </body>
    '''

    def clear_sky():
        return
        f"""<head><title>Meteo</title>
                <meta charset=utf-8>
            </head>
            <body>
                <h3>Le ciel est totalement dégagé au {adresse},
                et la température est de {temp}°C.</h3>
                <h3> Le ciel pourrait ressembler à : </h3>
                <img src="../images/clear_sky.png" width="400px">
            </body>"""

    def mainly_clear():
        return

    def fog():
        return

    def drizzle():
        return

    def freezing_drizzle():
        return

    def rain():
        return

    def freezing_rain():
        return

    def snow_fall():
        return

    def snow_grains():
        return

    def rain_shower():
        return

    def snow_shower():
        return

    def thunderstorm():
        return

    def thunderstorm_hail():
        return