class No:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None



def adicionar(lista, jogador):
    jogador = No(jogador)
    if lista == None:
        lista = jogador
        return lista

    else:
        jogador.proximo = lista
        lista = jogador
        return lista


def final (lista, jogador):
    novo = No(jogador)
    aux = lista
    if lista == None:
        lista = jogador
        return lista

    else:
        while aux.proximo != None:
            aux = aux.proximo

        aux.proximo = novo
        return lista

def mostrar(jogador):
    if jogador == None:
        print("sem jogadores :(")
        return None

    while jogador != None:
        print(jogador.jogador)
        jogador = jogador.proximo


def percorrer(atual, jogador):
    atual = No(jogador)
    print(atual.jogador)
    atual = atual.proximo
    return atual




def menu():
    print("1 - adicionar jogador")
    print("2 - mostrar lista")


def main():
    lista = None
    opc = 0
    while opc != 5:
        menu()
        opc = int(input("qual a opção? "))
        if opc == 1:
            jogador = input("qual o nome do jogador? ")
            lista = adicionar(lista, jogador)
        elif opc == 2:
            mostrar(lista)
        elif opc == 3:
            jogador = input("qual o nome do jogador? ")
            lista = final(lista, jogador)
        elif opc == 4:
            atual = percorrer(atual, jogador)

main()
