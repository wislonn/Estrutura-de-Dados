class No:
    def __init__(self, pessoa, responsavel):
        self.pessoa = pessoa
        self.proximo = None
        self.responsavel = responsavel


def add(pessoa, responsavel, lista):
    no = No(pessoa, responsavel)
    no.proximo = lista
    return no

def mostrar(lista, pessoa, responsavel):
    if lista == None:
        print("lista vazia")
        return None 
    aux = lista
    while aux != None:
        print("nome:",aux.pessoa)
        print("responsavel:", aux.responsavel)
        print ("---")
        aux = aux.proximo
    return lista
     
    
def remover(pessoa, responsavel, lista):
    if lista == None:
        print("lista vazia")
        return None

    if lista.pessoa == pessoa:
        return lista.proximo

    aux = lista

    while aux.proximo != None:
        if aux.proximo.pessoa == pessoa:
            aux.proximo = aux.proximo.proximo
            return lista

        aux = aux.proximo

    print("pessoa não encontrada")
    return lista


def menu():
    print ("1 - adicionar")
    print ("2 - listar")
    print ("3 - remover")
    opc = int (input("qual a opção? "))
    return opc

def main():
    opc = 0
    lista = None
    while opc != 4:
        opc = menu()
        if opc == 1:
            pessoa = input("quem quer adicionar? ")
            responsavel = input("pelo que ele é responsável? ")
            lista = add(pessoa, responsavel, lista)
        elif opc == 2:
            lista = mostrar(lista, pessoa, responsavel)
        elif opc == 3:
            pessoa = input("quem quer remover? ")
            responsavel = input("pelo que ele é responsável? ")
            lista = remover(pessoa, responsavel, lista)
         

main()
