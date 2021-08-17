from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from HQ_Mangás_e_Graphic_Novels import *
from Esportes_Lazer import *
from Sociedade_e_Ciências_Sociais import *
from Literatura import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
class salvar_HQ(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    IBMS = db.Column(db.String,)
    Capa = db.Column(db.String)
    Nome = db.Column(db.String)
    Autor = db.Column(db.String)
    Paginas = db.Column(db.String)
    Editora = db.Column(db.String)
class salvar_Esportes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    IBMS = db.Column(db.String,)
    Capa = db.Column(db.String)
    Nome = db.Column(db.String)
    Autor = db.Column(db.String)
    Paginas = db.Column(db.String)
    Editora = db.Column(db.String)
class salvar_Literatura(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    IBMS = db.Column(db.String,)
    Capa = db.Column(db.String)
    Nome = db.Column(db.String)
    Autor = db.Column(db.String)
    Paginas = db.Column(db.String)
    Editora = db.Column(db.String)
class salvar_Ciências_Sociais(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    IBMS = db.Column(db.String,)
    Capa = db.Column(db.String)
    Nome = db.Column(db.String)
    Autor = db.Column(db.String)
    Paginas = db.Column(db.String)
    Editora = db.Column(db.String)
db.create_all()
if __name__=="__main__":
    print("genero 1: HQ, Mangás e Graphic Novels")
    print("genero 2: Esportes e Lazer")
    print("genero 2: Literatura")
    print("genero 2: Sociedade e Ciências Sociais")
    x=float(input("genero 1, 2, 3 ou 4: "))
    n=0
    if x==1:
        ibsm, capa, nome, autor, paginas, editora=str(input("digite a ISBN, capa, nome, autor, paginas e editora: ")).split()
        nova=salvar_HQ(IBMS=ibsm, Capa=capa, Nome=nome, Autor=autor, Paginas=paginas, Editora=editora)
        db.session.add(nova)
        db.session.commit()
        todas= db.session.query(salvar_HQ).all()
        for p in todas:
            n=n+1
            pi=salvar_h1(p.IBMS, p.Capa, p.Nome, p.Autor, p.Paginas, p.Editora)
            print(pi.json())
    if x==2:
        ibsm, capa, nome, autor, paginas, editora=str(input("digite a ISBN, capa, nome, autor, paginas e editora: ")).split()
        nova1=salvar_Esportes(IBMS=ibsm, Capa=capa, Nome=nome, Autor=autor, Paginas=paginas, Editora=editora)
        db.session.add(nova1)
        db.session.commit()
        todas1= db.session.query(salvar_Esportes).all()
        for p1 in todas1:
            n=n+1
            pi1=salvar_h2(p1.IBMS, p1.Capa, p1.Nome, p1.Autor, p1.Paginas, p1.Editora)
            print(pi1.json())
    if x==3:
        ibsm, capa, nome, autor, paginas, editora=str(input("digite a ISBN, capa, nome, autor, paginas e editora: ")).split()
        nova2=salvar_Literatura(IBMS=ibsm, Capa=capa, Nome=nome, Autor=autor, Paginas=paginas, Editora=editora)
        db.session.add(nova2)
        db.session.commit(  )
        todas2= db.session.query(salvar_Literatura).all()
        for p2 in todas2:
            n=n+1
            pi2=salvar_h3(p2.IBMS, p2.Capa, p2.Nome, p2.Autor, p2.Paginas, p2.Editora)
            print(pi2.json())
    if x==4:
        ibsm, capa, nome, autor, paginas, editora=str(input("digite a ISBN, capa, nome, autor, paginas e editora: ")).split()
        nova3=salvar_Ciências_Sociais(IBMS=ibsm, Capa=capa, Nome=nome, Autor=autor, Paginas=paginas, Editora=editora)
        db.session.add(nova3)
        db.session.commit(  )
        todas3= db.session.query(salvar_Ciências_Sociais).all()
        for p3 in todas3:
            n=n+1
            pi3=salvar_h4(p3.IBMS, p3.Capa, p3.Nome, p3.Autor, p3.Paginas, p3.Editora)
            print(pi3.json())



