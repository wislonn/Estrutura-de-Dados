class No:
    def __init__(self, atleta):
        self.atleta = atleta
        self.proximo = None
        self.anterior = None




def inserir(lista, atleta):
    no = No(atleta)

    if lista == None:
        no.proximo = no
        no.anterior = no
        lista = no
        return lista

    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    print (lista.atleta)
    return lista


def remover(lista, atleta):
    if lista is None:
        print("lista vazia")
        return lista

    aux = lista

    while True:
        if aux.atleta == atleta:

            if aux.proximo == aux:
                print("unico elemento na lista")
                return None

            elif aux == lista:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                lista = aux.proximo
                return lista

            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista

        aux = aux.proximo

        if aux == lista:
            print("Atleta não encontrado")
            return lista


def mostrar(lista, atleta):
    if lista is None:
        print("Lista vazia")
        return

    aux = lista

    while True:
        print(aux.atleta)
        aux = aux.proximo

        if aux == lista:
            return lista


def proximo(lista):
    if lista is None:
        print("Lista vazia")
        return lista

    lista = lista.proximo
    print("o bastão está com:", lista.atleta)

    return lista


def menu():
    print ("1 - inserir atleta")
    print ("2 - remover atleta")
    print ("3 - proximo turno")
    print ("4 - mostrar quem tem o bastão")
    print ("5 - sair")
    opc = int(input("escolha a opção: "))
    return opc




def main ():
    opc = 0
    lista = None
    while opc != 5:
        opc = menu()
        if opc == 1:
            atleta = (input("qual o nome do cara? "))
            lista = inserir(lista, atleta)
        elif opc == 2:
            atleta = (input("quem quer tirar? "))
            lista = remover (lista, atleta)
        elif opc == 3:
            lista = proximo(lista)
        elif opc == 4:
            lista = mostrar(lista, atleta)
            


main()    
