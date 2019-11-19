# Aula 8 - 18-11-19
# web

from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem Vindos ao mundo real meus quiridus'

app.run()