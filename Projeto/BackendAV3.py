from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, jsonify, request, send_file
from werkzeug.wrappers import response
from flask_cors import CORS
from modeloL import *
import os

path = os.path.dirname(os.path.abspath(__file__))
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

@app.route("/login_usuario", methods=["POST"])
def login_usuario():#função para o usuario logar
    Cadados = request.get_json()
    Cad = db.session.query(Cadastro)\
        .filter(Cadastro.Email==Cadados['Email'], Cadastro.Senha==Cadados['Senha'])\
        .first() #busca no banco de dados as informaçoes
    if Cad:
        print("foi")
        resposta=jsonify({"resultado":"ok", "detalhes":Cad.json()})
        #se cad não for nulo, ele ira retornar os seus valores convertidos em json
    else:
        # informar mensagem de erro
        resposta=jsonify({"resultado":"erro", "detalhes": "Nao encontrado"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_livros")
def listar_livros():
    # obter as livros do cadastro
    livros = db.session.query(Biblioteca).all()
    # aplicar o método json que a classe livros possui a cada elemento da lista
    livros_em_json = [ x.json() for x in livros ]
    # converter a lista do python para json
    resposta = jsonify(livros_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/salvar_imagem", methods=['POST'])
def salvar_imagem():
    r = jsonify({"mensagem":"tentando..."})
    if request.method == 'POST':
        file_val = request.files['capa']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(path, 'Imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"mensagem":"ok", "arquivo": file_val.filename})
    r.headers.add("Access-Control-Allow-Origin", "*")
    return r
@app.route('/get_image/<int:id_livro>')
def get_image(id_livro):
    livro = db.session.query(Biblioteca).get(id_livro)
    # if request.args.get('type') == '1':
    #    filename = 'ok.gif'
    # else:
    #    filename = 'error.gif'
    arquivoimg = os.path.join(path, 'Imagens/'+ livro.Capa_do_livro)
    # arquivoimg = os.path.join('/home/ingguk/mysite/img_pet', livro.foto)
    # /home/ingguk/mysite/img_pet
    return send_file(arquivoimg, mimetype='image/gif')
@app.route("/deletar_livro/<int:delNomeLivro>", methods=['DELETE'])
def deletar_livro(delNomeLivro):
    #busca no banco de dados as informaçoes
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        # excluir a pessoa do ID informado
        Biblioteca.query.filter(Biblioteca.Idlivro == delNomeLivro).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
        # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!
       


"""@app.route("/listar_livros")
def listar_livros():
    lixta = []
    todas = db.session.query(delLivros).all()  # recebe as informaçoes de livros
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


app.run(debug=True)
