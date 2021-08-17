class salvar_h1:
    def __init__(self, ISBN='', Capa='', nome='', autor='', paginas='', editora=''):
        self.ISBM=ISBN
        self.Capa=Capa
        self.nome=nome
        self.autor=autor
        self.paginas=paginas
        self.editora=editora
    def __str__(self):
        return f'{self.ISBM}, {self.Capa}, {self.nome}, {self.autor}, {self.paginas}, {self.editora}'
    def json(self):
        return{
            "ISBM" : self.ISBM,
            "Capa" : self.Capa,
            "nome" : self.nome,
            "autor" : self.autor,
            "paginas" : self.paginas,
            "editora" : self.editora,
        }