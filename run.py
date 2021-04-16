"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo desde Flask</h1>"
    return "<h1>Snrosales</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
    resultado = 10 + 10
    return "<ul><li>FC. Barcelona</li><li>Real Madrid</li><li>Real Betis</li><li>Atlético de Madrid</li></ul>"
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
