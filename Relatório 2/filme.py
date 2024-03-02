from typing import Any


class Filme:
    #O filme deve contendo título, ano de lançamento, diretor(a), gênero e duração).
    def __init__(self,titulo,ano,diretor,genero,duracao):
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao
        pass
    
    def get_titulo(self):
        return self.titulo
    
    def get_ano(self):
        return self.ano
    
    def get_diretor(self):
        return self.diretor
    
    def get_genero(self):
        return self.genero
    
    def get_duracao(self):
        return self.duracao

    def infos_filme(self):
        print(f"Titulo: {self.titulo}")
        print(f"Ano: {self.ano}")
        print(f"Diretor: {self.diretor}")
        print(f"Genero: {self.genero}")
        print(f"Duração: {self.duracao} min")