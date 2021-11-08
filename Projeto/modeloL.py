from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "livros.db") #recebe o caminho do arquivo livros.db
db= SQLAlchemy(app)


class Biblioteca(db.Model):
    Idlivro = db.Column(db.Integer, primary_key=True)
    ISBN= db.Column(db.Integer)
    Capa_do_livro=db.Column(db.String)
    Nome_do_livro= db.Column(db.String)
    Autor= db.Column(db.String)
    Paginas =db.Column(db.Integer)
    Editora=db.Column(db.String)
    Status=db.Column(db.String)
    def __str__(self):
        return f'{str(self.Idlivro)}, {str(self.ISBN)}, {self.Capa_do_livro}, {self.Nome_do_livro}, {self.Autor}, {str(self.Paginas)}, {self.Editora}, {self.Status}'
    
    def json(self):
        return{
            "Idlivro" : self.Idlivro,
            "ISBN": self.ISBN,
            "Capa_do_livro": self.Capa_do_livro,
            "Nome_do_livro" : self.Nome_do_livro,
            "Autor" : self.Autor,
            "Paginas": self.Paginas,
            "Editora": self.Editora,
            "Status": self.Status
            #retorna em join as informaçoes
        }
class Cadastro(db.Model):
    Idcad = db.Column(db.Integer, primary_key=True)
    Nome= db.Column(db.String)
    Idade=db.Column(db.String)
    Email= db.Column(db.String, unique=True)
    Senha= db.Column(db.String)
    Repetir_senha =db.Column(db.String)
    def __str__(self):
        return f'{str(self.Idcad)}, {str(self.Nome)}, {self.Idade}, {self.Email}, {self.Senha}, {str(self.Repetir_senha)}'
    
    def json(self):
        return{
            "Idcad" : self.Idcad,
            "Nome": self.Nome,
            "Idade": self.Idade,
            "Email" : self.Email,
            "Senha" : self.Senha,
            "Repetir_senha": self.Repetir_senha,
            #retorna em join as informaçoes
        }

class Editora(db.Model):#classe para informar a editora de determinado livro
    id_editora=db.Column(db.Integer, primary_key=True)#cria a chave primaria
    NomeEditora=db.Column(db.String)
    NacionalidadeEditora=db.Column(db.String)
    EndereçoEditora=db.Column(db.String)
    #acima cria as colunas necessarias
    def __str__(self):
        return f'{str(self.id_editora)}, {self.NomeEditora}, {self.NacionalidadeEditora}, {self.EndereçoEditora}'
    
    def json(self):
        return{
            "Ideditora" : self.id_editora,
            "Nome da editora": self.NomeEditora,
            "Nacionalidade da editora" : self.NacionalidadeEditora,
            "Endereco da Editora" : self.EndereçoEditora,
            #retorna em join as informaçoes
        }    

class Autor_livro(db.Model):#classe para informar o autor de determinado livro
    id = db.Column(db.Integer, primary_key=True)#cria a chave primaria
    NomeAutor=db.Column(db.String)
    IdadeAutor=db.Column(db.String)
    PaisOrigem=db.Column(db.String)
    #acima cria as colunas necessarias  
    def __str__(self):
        return f'{str(self.id)}, {self.NomeAutor}, {self.IdadeAutor}, {self.PaisOrigem}'
    
    def json(self):
        return{
            "id" : self.id,
            "Nome do Autor": self.NomeAutor,
            "Idade do Autor" : self.IdadeAutor,
            "Pais em que o autor nasceu" : self.PaisOrigem,
            #retorna em join as informaçoes
        } 

class livros(db.Model):#classe para cadastrar o livro, classe pai
    Idlivro = db.Column(db.Integer, primary_key=True)
    ImagemCapa= db.Column(db.String)
    Nome= db.Column(db.String)
    AutorID= db.Column(db.Integer, db.ForeignKey(Autor_livro.id))
    Autor = db.relationship('Autor_livro')#cria uma chave secundaria, que faz referencia com a id do autor
    LeituraStatus=db.Column(db.String)
    IdEditora= db.Column(db.Integer, db.ForeignKey(Editora.id_editora))
    editora = db.relationship('Editora')#cria uma chave secundaria, que faz referencia com a id da editora
    NumeroPaginas=db.Column(db.String)
    PaginasLidas=db.Column(db.String)
    type = db.Column(db.String(50)) # Discriminador
    __mapper_args__ = {
        'polymorphic_identity':'livros', 
        'polymorphic_on':type # nome do campo que vincula os filhos
    }
    def __str__(self):
        return f'{str(self.Idlivro)}, {self.ImagemCapa}, {self.Nome}, {str(self.Autor)}, {self.LeituraStatus}, {str(self.editora)}, {self.NumeroPaginas}, {self.PaginasLidas}'
    

class Estou_Lendo(livros):#classe filho que indica que o usuario ainda esta lendo esse livro
    Tempo_de_leitura=db.Column(db.String)
    PaginasQueFalta=db.Column(db.String)
    __mapper_args__ = { 
        'polymorphic_identity':'estou_lendo', # Tipo que distingue entre "ja li", "parei de ler", "lendo" 
    }

    def __str__(self):
        return f'{str(self.Idlivro)}, {self.ImagemCapa}, {self.Nome}, {str(self.Autor)}, {self.LeituraStatus}, {str(self.editora)}, {self.NumeroPaginas}, {self.PaginasLidas}, {self.Tempo_de_leitura}, {self.PaginasQueFalta}, {self.type}'
    
    def json(self):
        return{
            "Idlivro" : self.Idlivro,
            "ImagemCapa": self.ImagemCapa,
            "Nome" : self.Nome,
            "idAutor" : self.Autor.json(),
            "LeituraStatus" : self.LeituraStatus,
            "InfoEditora" : self.editora.json(),
            "NumeroPaginas" : self.NumeroPaginas,
            "Paginas Lidas" : self.PaginasLidas,
            "tempo de leitura" : self.Tempo_de_leitura,
            "Paginas que faltam ler" : self.PaginasQueFalta
            #retorna em join as informaçoes
        }    

class Ja_li(livros):#classe filho que indica que o usuario ja leu esse livro
    DiasPraTerminar=db.Column(db.String)
    avaliação=db.Column(db.String)
    AddFavorito=db.Column(db.String)
    RecomendarMais=db.Column(db.String)
    __mapper_args__ = { 
        'polymorphic_identity':'ja_li', # Tipo que distingue entre "ja li", "parei de ler", "lendo" 
    }
    def __str__(self):
        return f'{str(self.Idlivro)}, {self.ImagemCapa}, {self.Nome}, {str(self.Autor)}, {self.LeituraStatus}, {str(self.editora)}, {self.NumeroPaginas}, {self.PaginasLidas}, {self.DiasPraTerminar}, {self.avaliação}, {self.AddFavorito}, {self.RecomendarMais}, {self.type}'
    
    def json(self):
        return{
            "Idlivro" : self.Idlivro,
            "ImagemCapa": self.ImagemCapa,
            "Nome" : self.Nome,
            "idAutor" : self.Autor.json(),
            "LeituraStatus" : self.LeituraStatus,
            "InfoEditora" : self.editora.json(),
            "NumeroPaginas" : self.NumeroPaginas,
            "PaginasLidas" : self.PaginasLidas,
            "Dias que faltam para terminar":self.DiasPraTerminar,
            "avaliacao do livro":self.avaliação,
            "Adicionar aos favoritos" : self.AddFavorito,
            "Recomendar mais" : self.RecomendarMais
            #retorna em join as informaçoes
        }

class Parei_de_ler(livros):#classe filho que indica que o usuario parou de ler esse livro
    PQparou=db.Column(db.String)
    PaginasFaltam=db.Column(db.String)
    __mapper_args__ = { 
        'polymorphic_identity':'parei_de_ler', # Tipo que distingue entre "ja li", "parei de ler", "lendo" 
    }
    def __str__(self):
        return f'{str(self.Idlivro)}, {self.ImagemCapa}, {self.Nome}, {str(self.Autor)}, {self.LeituraStatus}, {str(self.editora)}, {self.NumeroPaginas}, {self.PaginasLidas}, {self.PQparou}, {self.PaginasFaltam}, {self.type}'
    
    def json(self):
        return{
            "Idlivro" : self.Idlivro,
            "ImagemCapa": self.ImagemCapa,
            "Nome" : self.Nome,
            "idAutor" : self.Autor.json(),
            "LeituraStatus" : self.LeituraStatus,
            "InfoEditora" : self.editora.json(),
            "NumeroPaginas" : self.NumeroPaginas,
            "PaginasLidas" : self.PaginasLidas,
            "Por que parou de ler" : self.PQparou,
            "Pagina em que parou" : self.PaginasFaltam
            #retorna em join as informaçoes
        }

#if __name__=="__main__":#testa as classes
#    if os.path.exists(arquivobd):
#        os.remove(arquivobd)#remove o banco de dados se existir
#        print("pepe")
    db.create_all()#cria o banco de dados
    #u1=Editora(NomeEditora="Mosaico", NacionalidadeEditora="Brasileira", EndereçoEditora="rua fulano de tal")
    #u2=Autor_livro(NomeAutor="Pinoquio", IdadeAutor='56', PaisOrigem="Inglaterra")
    #u21=Autor_livro(NomeAutor="JK", IdadeAutor='64', PaisOrigem="Inglaterra")
    #u3=Estou_Lendo(ImagemCapa="semimagem", Nome="pequeno princepe", Autor=u2, LeituraStatus="lendo", editora=u1, NumeroPaginas="195", PaginasLidas="190", Tempo_de_leitura="40min", PaginasQueFalta="5")
    #u4=Ja_li(ImagemCapa="semimagem", Nome="pequeno princepe2", Autor=u2, LeituraStatus="ja li", editora=u1, NumeroPaginas="205", PaginasLidas="190", DiasPraTerminar="30", avaliação="bom", AddFavorito="Nao", RecomendarMais="nao")
    #u5=Parei_de_ler(ImagemCapa="semimagem", Nome="Harry Potter", Autor=u21, LeituraStatus="Parei de ler", editora=u1, NumeroPaginas="1005", PaginasLidas="405", PQparou="Achei chato", PaginasFaltam="405")
    #ur=u3, u4, u5
    #db.session.add(u1)
    #db.session.add(u2)
    #db.session.add(u21)
    #db.session.add(u3)
    #db.session.add(u4)
    #db.session.add(u5)
    #db.session.commit()
    #TodosPessoa = db.session.query(livros).all()#recebe as informaçoes de livros
    #for i in TodosPessoa:
    #    print(i.json())#printa em json a tebela livros
    TodosPessoa = db.session.query(Cadastro).all()
    for i in TodosPessoa:
        print(i.json())
        print(i.Email)
    #p=Cadastro.query.filter_by (Nome = 'Marcos')
    #print(p)
    python = Biblioteca(ISBN="123", Capa_do_livro="", Nome_do_livro="Python turbinado", Autor="Jack John", Paginas=400, Editora = "Atenas")
    db.session.add(python)
    db.session.commit()
    #print(python)
    #print(python.json())