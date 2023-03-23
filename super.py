from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
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

@app.route('/address', methods=['POST'])
def address():
    user_address = request.form['address']
    if user_address == "NYC" :
        return render_template("fog.html")
    # Utilisez user_address pour générer le contenu HTML de votre choix
    return f"<h1>Voici le contenu généré pour l'adresse : {user_address}</h1>"

if __name__ == '__main__':
    app.run(debug=True)