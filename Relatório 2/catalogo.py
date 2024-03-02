from filme import Filme

class Catalago:
    def __init__(self):
        self.filmes = []
        pass

    #O sistema deve possibilitar o cadastro de filmes (contendo título, ano de lançamento, diretor(a), gênero e duração).
    def add_filme(self, filme):
        self.filmes.append(filme)

    #Também deve possibilitar a listagem dos filmes cadastrados
    def list_filmes(self):
        for Filme in self.filmes:
            Filme.infos_filme()
            print("============================")
    
    #permitindo o filtro e ordenação por ano de lançamento, gênero e diretor.
    def busca_filme(self, criterio, valor):
        for filme in self.filmes:
            if criterio == "ano" and filme.get_ano() == valor:
                print(filme.infos_filme())
                break
            elif criterio == "genero" and filme.get_genero() == valor:
                print(filme.infos_filme())
                break
            elif criterio == "diretor" and filme.get_diretor() == valor:
                print(filme.infos_filme())
                break
            else:
                print("nenhum filme encontrado")
    
    def busca_ano(self,ano):
        for Filme in self.filmes:
            if Filme.get_ano() == ano:
                print(Filme.infos_filme())

    def busca_genero(self,genero):
        for Filme in self.filmes:
            if Filme.get_genero() == genero:
                print(Filme.infos_filme())
        
    def busca_diretor(self,diretor):
        for Filme in self.filmes:
            if Filme.get_diretor() == diretor:
                print(Filme.infos_filme())
    