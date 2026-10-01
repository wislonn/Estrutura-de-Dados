class No:
    def __init__(self, serv, id, stts):
        self.serv = serv
        self.id = id
        self.stts = stts
        self.proximo = None
        self.anterior = None







def add(no, lista):
    if lista == None:
        lista = no
        return lista
    no.proximo = lista
    lista.anterior = no
    lista = no
    return lista

def mostrar(lista, direcao):
    aux = lista
    if lista == None:
        print("lista vazia")
    if direcao == 1:
        while aux != None:
            print (aux.serv, "id:", aux.id)
            if aux.stts == 1:
                print("status: ligado")
            if aux.stts == 2:
                print("status: desligado")
            print("--------------")
            aux = aux.proximo
    if direcao == 2:
        while aux.proximo != None:
            aux = aux.proximo
        while aux != None:
            print (aux.serv, "id:", aux.id)
            if aux.stts == 1:
                print("status: ligado")
            if aux.stts == 2:
                print("status: desligado")
            print("--------------")
            aux = aux.anterior
    return lista


def remover(tirar, lista):
    if lista == None:
        print("ta vazia a lista")
        return None
    aux = lista
    while aux.serv != tirar:
        aux = aux.proximo
    if aux.proximo == None:
        aux.anterior.proximo = None
        return lista
    if aux.proximo != None and aux.anterior != None:
        aux.anterior.proximo = aux.proximo
        aux.proximo.anterior = aux.anterior
        return lista
    if aux == lista:
        lista = aux.proximo
        return lista
    if aux.proximo == None == aux.anterior:
        lista = None
        return lista
    print("não encontrado")
    return lista

def status(alt, lista):
    aux = lista
    while aux.serv != alt:
        aux = aux.proximo
    if aux.stts == 1:
        aux.stts = 2
        return lista
    if aux.stts == 2:
        aux.stts = 1
    print("item não encontrado")
    return lista
    



def menu():
    print("1 - inserir")
    print("2 - remover")
    print("3 - ligar/desligar")
    print("4 - percorrer lista")
    print("5 - sair")
    opc = int(input("qual opção? "))
    return opc

def main(): 
    opc = 0
    lista = None
    while opc != 5:
        opc = menu()
        if opc == 1:
            serv = input("qual o nome do servidor? ")
            id = int(input("qual o id? "))
            stts = int(input("status: 1 = ligado 2 = desligado -- "))
            no = No(serv, id, stts)
            lista = add(no, lista)

        elif opc == 2:
            tirar = input("qual o servidor que voce quer remover? ")
            lista = remover(tirar, lista)

        elif opc == 3:
            alt = input("qual o servidor voce quer alterar? ")
            lista = status(alt, lista)

        elif opc == 4:
            print("1 - frente")
            print("2 - trás")
            direcao = int(input("para frente ou para trás?"))
            mostrar(lista, direcao)
main()
