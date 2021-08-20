from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, jsonify
from modelo import *
@app.route("/")
def padrao():
    return "backend funciona"
@app.route("/listar_livros")
def listar_livros():
    lixta=[]
    todas= db.session.query(livros).all()#recebe as informaçoes de livros
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)#transforma a lixta em json
    return resposta
@app.route("/listar_autor")
def listar_autor():
    lixta=[]
    todas= db.session.query(Autor_livro).all()#recebe as informaçoes de livros
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)#transforma a lixta em json
    return resposta
@app.route("/listar_editora")
def listar_editora():
    lixta=[]
    todas= db.session.query(Editora).all()#recebe as informaçoes de livros
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)#transforma a lixta em json
    return resposta
app.run(debug=True)