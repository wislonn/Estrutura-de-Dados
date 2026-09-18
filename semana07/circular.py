class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


def adicionar(dado, lista, atual):
    no = No(dado)
    if lista == None:
        lista = no
        no.proximo = no
        no.anterior = no
        atual = lista
        return lista



    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    return lista


def seguir(atual):
    print(atual.dado)
    atual = atual.proximo




def menu():
    print("1 - adicionar dado")
    print("2 - seguir")


def main():
    lista = None
    opc = 0
    atual = 0
    while opc != 3:
        menu()
        opc = int(input("digite a opção: "))
        if opc == 1:
            dado = int(input("qual numero? "))
            lista = adicionar(dado, lista, atual)
        elif opc == 2:
            atual = seguir(atual)


main()
