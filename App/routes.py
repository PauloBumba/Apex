from App import api
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
usuarios_registrados={}
@api.route("/")
def Registro():
    return render_template('Registro.html')
@api.route("/login",methods=['GET'])
def login():
    return render_template('login.html')
@api.route('/autenticar', methods=['GET'])
def autenticar():
    email = request.args.get('email')
    cpf= request.args.get('cpf')
    if email in usuarios_registrados and usuarios_registrados[email]['senha'] == cpf:
        # Autenticação bem-sucedida, redirecione para a página 'index'
        return redirect(url_for('rec'))
    else:
        # Autenticação falhou, redirecione de volta para a página de login
        return redirect(url_for('index'))

@api.route('/validação', methods=['GET'])
def validação ():
    email = request.args.get('email')
    cpf= request.args.get('cpf')
    # Armazene as informações do usuário no dicionário
    if email in usuarios_registrados.keys():
        return redirect(url_for('rec'))

    # Armazene as informações do usuário no dicionário
    usuarios_registrados[email] = {'senha': cpf}
    # Redirecione para a página de login (ou apropriada)
    return redirect(url_for('login'))


@api.route("/index",methods=['GET'])
def index():
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
@api.route("/rec")
def rec():
    return render_template("rec.html")


