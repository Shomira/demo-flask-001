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
    resultado = "10 + 10"
    return "<h2>Practica 2</h2><h3>Listado de Nombres</h3><ul><li>  Niñas <ul><li>Sheccid J.</li><li>Dannielle A.</li><li>Shields R.</li><li>Jossie H.</li></ul></li><li>Niños<ul><li>Drake J.</li><li>Matwei M.</li><li>Marshall D.</li><li>Derek S.</li></ul></li></ul>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
