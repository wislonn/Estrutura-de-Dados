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

def mostrar(jogador):
    if jogador == None:
        print("sem jogadores :(")
        return None

    while jogador != None:
        print(jogador.jogador)
        jogador = jogador.proximo


def menu():
    print("1 - adicionar jogador")
    print("2 - mostrar lista")


def main():
    lista = None
    opc = 0
    while opc != 3:
        menu()
        opc = int(input("qual a opção? "))
        if opc == 1:
            jogador = input("qual o nome do jogador? ")
            lista = adicionar(lista, jogador)
        elif opc == 2:
            mostrar(lista)

main()
