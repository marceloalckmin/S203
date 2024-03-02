from filme import Filme
from catalogo import Catalago

catalogo = Catalago()

while True:
    print("Bem vindo ao nosso catálogo de filmes!")
    print("1 para adicionar filmes")
    print("2 para ver nosso catálogo completo")
    print("3 para buscar um filme")
    print("4 para sair")

    op = input("Digite a funcionalidade que deseja:")

    if op == "1":
        titulo = input("Digite o titulo do filme: ")
        ano = input("Ano de lançamento: ")
        genero = input("Genero: ")
        diretor = input("Diretor: ")
        duracao = input("Duracao: ")

        filme = Filme(titulo,ano,genero,diretor,duracao)
        catalogo.add_filme(filme)
        print("Prontinho! Adicionado!")

    elif op == "2":
        print("Lista de filmes: ")
        print(catalogo.list_filmes())

    elif op == "3":
        print("Digite 'ano' se quiser buscar por ano de lançamento")
        print("Digite 'genero' se quiser buscar por genero")
        print("Por fim digite 'diretor' se quiser buscar por diretor")
        escolha = input("Digite sua escolha: ")
        print("Agora qual ano/genero/diretor quer buscar?")
        busca = input()
        print(catalogo.busca_filme(escolha,busca))
    
    elif op == "4":
        print("Obrigado e volte sempre!")
        break

    else: 
        print('Digite um valor válido.')
