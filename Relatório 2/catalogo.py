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
    