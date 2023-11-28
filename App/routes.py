from App import api
from flask import Flask
from flask import render_template
from flask import Request
@api.route("/index")
@api.route("/")
def Homepage():
    return render_template('index.html')

@api.route("/Equipes")
def Equipes():
    return render_template('Equipes.html')

@api.route("/Computação")
def Ciencia_Computaçãõ():
    return render_template('Acapuc.html')

@api.route("/Calendario")
def Computação():
    return render_template('Calendario.html')
@api.route("/Resultado")
def Result():
    return render_template('resultado.html')
@api.route("/Sobre")
def Sobre():
    return render_template("Sobre.html")
