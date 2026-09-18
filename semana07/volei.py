class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def add_ini(nome, lista):
    no = No(nome)
    if lista == None:
        lista = no
        return lista

    lista.anterior = no
    no.proximo = lista
    lista = no
    return lista

def percorrer_frente(lista):
    aux = lista
    if lista == None:
        print("no players :(")

    while aux != None:
        print(aux.nome)
        aux = aux.proximo
    return lista

def percorrer_tras(lista):
    aux = lista
    if lista == None:
        print("no players :(")

    while aux.proximo != None:
        aux = aux.proximo

    while aux != None:
        print (aux.nome)
        aux = aux.anterior
    return lista


def menu():
    print("1 - add inicio")
    print("2 - percorrer frente")
    print("3 - percorrer tras")


def main():
    opc = 0
    lista = None
    while opc != 4:
        menu()
        opc = int(input("qual opção? "))
        if opc == 1:
            nome = (input("qual o nome do cara? "))
            lista = add_ini(nome, lista)
        elif opc == 2:
            percorrer_frente(lista)
        elif opc == 3:
            percorrer_tras(lista)


main()
