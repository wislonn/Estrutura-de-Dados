class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def inserir(pilha, dado):
    no = No(dado)
    if pilha == None:
        pilha = no
        return pilha
    no.proximo = pilha
    pilha = no
    return pilha

def remover(pilha):
    if pilha == None:
        print("lista vazia")
        return None

    print("removido:", pilha.dado)
    pilha = pilha.proximo

    return pilha

def mostrar(pilha):
    if pilha == None:
        print("pilha vazia")
        return
    print(pilha.dado)

def mostrarr(pilha):
    contador = 1
    aux = pilha

    while aux != None:
        print (contador, " - ", aux.dado)
        contador += 1
        aux = aux.proximo

    



def menu():
    print("1 - Inserir operação na pilha")
    print("2 - Retirar última operação")
    print("3 - Mostrar última operação inserida")
    print("4 - Mostrar todas as operações pendentes")
    print("5 - Sair")
    print("---------")
    opc = int(input("qual opc? "))
    return opc

def main():
    opc = 0
    dado = 0
    pilha = None
    while opc != 5:
        opc = menu()
        if opc == 1:
            dado = input("qual a conta? ")
            pilha = inserir(pilha, dado)
        elif opc == 2:
            pilha = remover(pilha)
        elif opc == 3:
            mostrar(pilha)
        elif opc == 4:
            mostrarr(pilha)
        elif opc == 5:
            print("saiu")

main()
