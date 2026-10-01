class No:
    def __init__(self, deploy, duracao, ambi, stts):
        self.deploy = deploy
        self.duracao = duracao
        self.ambi = ambi
        self.stts = stts
        self.anterior = None
        self.proximo = None





def listar(lista, opp):
    aux = lista
    if opp == 1:
        while True:

            if aux.ambi == 1:
                print(aux.deploy, "ambiente: teste")

            aux = aux.proximo

            if aux == lista:
                break
        while True:

            if aux.ambi == 2:
                print(aux.deploy, "ambiente: homologação")

            aux = aux.proximo

            if aux == lista:
                break
        while True:

            if aux.ambi == 3:
                print(aux.deploy, "ambiente: produção")

            aux = aux.proximo

            if aux == lista:
                break
        return lista
    if opp == 2:
        while True:

            if aux.stts == 1:
                print(aux.deploy)

            aux = aux.proximo
            if aux == lista:
                break
        return lista


def add(lista, no):
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
    return lista 

def tempo(lista):
    aux = lista
    total = 0
    while True:
        print(aux.deploy, "tempo: ", aux.duracao)
        aux = aux.proximo
        total += aux.duracao
        if aux == lista:
            print("tempo total:", total)
            return lista

def ativar(qual, lista):
    aux = lista
    if qual != aux:
        aux = aux.proximo
    if aux.stts == 1:
        print("ja ta ativado")
        return lista
    elif aux.stts == 2:
        aux.stts = 1
        return lista

def desativar(qual, lista):
    aux = lista
    if qual != aux:
        aux = aux.proximo
    if aux.stts == 2:
        print("ja ta desativado")
        return lista
    elif aux.stts == 1:
        aux.stts = 2
        return lista



def menu():
    print("1 - adicionar deploy")
    print("2 - listar deploys")
    print("3 - tempo total")
    print("4 - ativar um deploy")
    print("5 - desativar um deploy")
    print("")
    opc = int(input("qual opção? "))
    return opc

def main():
    lista = None
    opc = 0
    while opc != 7:
        opc = menu()
        if opc == 1:
            deploy = input("qual o nome do deploy? ")
            duracao = int(input("qual o tempo do deploy? "))
            print("1 - teste")
            print("2 - homologação")
            print("3 - produção")
            ambi = int(input("em que ambiente é? "))
            print("1 - ativado")
            print("2 - desativado")
            stts = int(input("qual o status?"))
            no = No(deploy, duracao, ambi, stts)
            lista = add(lista, no)
        elif opc == 2:
            print("1 - Listar os deploys na ordem: teste → homologação → produção")
            print("2 - Listar apenas os deploys ativos")
            opp = int(input("qual opção? "))
            lista = listar(lista, opp)
        elif opc == 3:
            lista = tempo(lista)
        elif opc == 4:
            qual = input("qual servidor voce quer ativar?")
            lista = ativar(qual, lista)
        elif opc == 5:
            qual = input("qual servidor voce quer ativar?")
            lista = ativar(qual, lista)

main()
