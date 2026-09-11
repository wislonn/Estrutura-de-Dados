class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None



def adicionar(inicio, fim, dado):
    novo = No(dado)

    if fim == inicio == None:
        inicio = novo
        fim = novo
        return fim, inicio
    fim.proximo = novo
    novo.anterior = fim
    fim = novo
    return inicio, fim


def atender (inicio, fim, dado):
    aux = inicio
    if inicio == None:
        print ("fila vazia")
        return None, None
    if inicio == fim:
        print (aux.dado,"ultimo da fila")
    print (inicio.dado, "foi atendido")
    inicio = inicio.proximo
    return inicio
    


def listar(inicio):
    contador = 1
    aux = inicio
    if inicio == None:
        print("Lista vaiza")
        return
    print (aux.dado, "é o primeiro da fila")
    while aux != None:
        contador += 1
        aux = aux.proximo
    print(contador, "pessoas na fila")




def menu():
    print("1 - adicionar pessoa")
    print("2 - atender")
    print("3 - listar")
    print("4 - sair")
    opc = int(input("qual opção? "))
    return opc


def main():
    dado = 0
    opc = 0
    fim = None
    inicio = None

    while opc != 4:
        opc = menu()
        if opc == 1:
            dado = input("nome do sujeito: ")
            inicio, fim = adicionar(inicio, fim, dado)
        elif opc == 2:
            inicio = atender(inicio, fim, dado)
        elif opc == 3:
            listar(inicio)









main()
