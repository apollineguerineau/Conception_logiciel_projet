class View:
    def __init__(self, adresse, temp):
        self.adresse = adresse
        self.temp = temp

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