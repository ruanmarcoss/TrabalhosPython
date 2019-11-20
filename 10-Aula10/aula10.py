# Aula 10 20-11-2019
# ---- Web - Calculadora 

nome_pagina = 'Calculadora'
from flask import Flask, render_template, request
from calculo_metodo import * 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['n1'])
    n2 = int(request.args['n2'])
    r_soma = soma(n1,n2)
    r_subtracao = subtracao(n1,n2)
    r_multiplicacao = multiplicacao(n1,n2)
    r_divisao_int = divisao_int(n1,n2)
    r_divisao_frac = divisao_frac(n1,n2)
    r_resto = resto(n1,n2)
    r_raiz = raiz(n1,n2)

    resultados = {'soma':r_soma, 'subtracao':r_subtracao, 'multiplicacao':r_multiplicacao, 'divisao_int':r_divisao_int, 'divisao_frac':r_divisao_frac, 'resto':r_resto, 'raiz':r_raiz }

    return render_template ('resultado.html',resultados=resultados)


app.run(host='192.168.0.90',port=80)