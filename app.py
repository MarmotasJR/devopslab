from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Essa aula e muito TOP! Obrigado prof! - Marmotas"

if __name__ == '__main__':
    app.run()