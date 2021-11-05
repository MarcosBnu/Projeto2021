from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, jsonify, request
from modeloL import *


@app.route("/")
def padrao():
    return "backend funciona"


@app.route("/incluir_livro", methods=["post"])
def incluir_livro():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json()  # (force=True) dispensa Content-Type na requisição
    try:  # tentar executar a operação
        # Biblioteca(ISBN="123", Capa_do_livro="livro de python", Nome_do_livro="Python turbinado", Autor="Jack John", Paginas=400, Editoras = "várias")
        nova = Biblioteca(**dados)  # criar a nova pessoa
        db.session.add(nova)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

@app.route("/cadastrar_usuario", methods=["post"])
def cadastrar_usuario():
    # preparar uma resposta otimista
    resposta_cad = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    Cadados = request.get_json()  # (force=True) dispensa Content-Type na requisição
    try:  # tentar executar a operação
        # Biblioteca(ISBN="123", Capa_do_livro="livro de python", Nome_do_livro="Python turbinado", Autor="Jack John", Paginas=400, Editoras = "várias")
        novaCad = Cadastro(**Cadados)  # criar a nova pessoa
        db.session.add(novaCad)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta_cad = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta_cad.headers.add("Access-Control-Allow-Origin", "*")
    return resposta_cad  # responder!


"""@app.route("/listar_livros")
def listar_livros():
    lixta = []
    todas = db.session.query(livros).all()  # recebe as informaçoes de livros
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)  # transforma a lixta em json
    return resposta


@app.route("/listar_autor")
def listar_autor():
    lixta = []
    # recebe as informaçoes de livros
    todas = db.session.query(Autor_livro).all()
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)  # transforma a lixta em json
    return resposta


@app.route("/listar_editora")
def listar_editora():
    lixta = []
    todas = db.session.query(Editora).all()  # recebe as informaçoes de livros
    for p in todas:
        lixta.append(p.json())
    resposta = jsonify(lixta)  # transforma a lixta em json
    return resposta"""


app.run() #debug=True)
