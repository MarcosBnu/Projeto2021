from flask_sqlalchemy import SQLAlchemy
from flask import Flask, json, jsonify
from HQ_Mangás_e_Graphic_Novels import *
from Esportes_Lazer import *
from Sociedade_e_Ciências_Sociais import *
from Literatura import *
from menu import *
x=float(input("numero: "))
@app.route("/")
def padrao():
    lixta=[]
    if x==1:
        no=0
        todas= db.session.query(salvar_HQ).all()
        for p in todas:
            pi=salvar_h1(p.IBMS, p.Capa, p.Nome, p.Autor, p.Paginas, p.Editora)
            lixta.append(pi.json())
        resposta = jsonify(lixta)
        return resposta
    if x==2:
        todas= db.session.query(salvar_Esportes).all()
        for p1 in todas:
            pi=salvar_h2(p1.IBMS, p1.Capa, p1.Nome, p1.Autor, p1.Paginas, p1.Editora)
            lixta.append(pi.json())
        resposta = jsonify(lixta)
        return resposta
    if x==3:
        todas= db.session.query(salvar_Literatura).all()
        for p in todas:
            pi=salvar_h3(p.IBMS, p.Capa, p.Nome, p.Autor, p.Paginas, p.Editora)
            lixta.append(pi.json())
        resposta = jsonify(lixta)
        return resposta
    if x==4:
        todas= db.session.query(salvar_Ciências_Sociais).all()
        for p in todas:
            pi=salvar_h4(p.IBMS, p.Capa, p.Nome, p.Autor, p.Paginas, p.Editora)
            lixta.append(pi.json())
        resposta = jsonify(lixta)
        return resposta
app.run(debug=True)