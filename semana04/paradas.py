class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None




def inserir(lista, parada):
    no = No(parada)

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
    print (lista.parada)
    return lista


def remover(lista, parada):
    if lista is None:
        print("lista vazia")
        return lista

    aux = lista

    while True:
        if aux.parada == parada:

            if aux.proximo == aux:
                print("unica parada na lista")
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
            print("parada não encontrada")
            return lista


def mostrar(lista, parada):
    if lista is None:
        print("Lista vazia")
        return

    aux = lista

    while True:
        print(aux.parada)
        aux = aux.proximo

        if aux == lista:
            return lista


def proximo(lista):
    if lista is None:
        print("Lista vazia")
        return lista

    print("o onibus chegou em", lista.parada)
    lista = lista.proximo
    print("a próxima parada é:", lista.parada)

    return lista


def menu():
    print ("1 - inserir parada")
    print ("2 - remover parada")
    print ("3 - proxima parada")
    print ("4 - mostrar paradas")
    print ("5 - sair")
    opc = int(input("escolha a opção: "))
    return opc




def main ():
    opc = 0
    lista = None
    while opc != 5:
        opc = menu()
        if opc == 1:
            parada = (input("qual o nome da parada? "))
            lista = inserir(lista, parada)
        elif opc == 2:
            parada = (input("qual parada quer tirar? "))
            lista = remover (lista, parada)
        elif opc == 3:
            lista = proximo(lista)
        elif opc == 4:
            lista = mostrar(lista, parada)
            
#era a mesma coisa do dos bastoes

main()    
