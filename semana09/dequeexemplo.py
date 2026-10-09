class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    def cabecamais(self, dado):
        novo = No(dado)

        if self.head == None:
            self.head = self.tail = novo
            return
        
        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo


    def caudamais(self, dado):
        novo = No(dado)

        if self.tail == None:
            self.tail = self.head = novo
            return


        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo
    

    def mostrarcabeca(self):
        if self.head == None:
            print("deque vazio")
            return
        aux = self.head
        while aux != None:
            print("- ", aux.dado)
            aux = aux.proximo

    def mostrarcauda(self):
        aux = self.tail
        if self.head == None:
            print("tudo vazio")
            return
        while aux != None:
            print ("- ", aux.dado)
            aux = aux.anterior


    def cabecamenos(self):
        self.head = self.head.proximo
        return

    def caudamenos(self):
        self.tail = self.tail.anterior
        self.tail.proximo = None
        return


def menu():
    print ("1 - inserir cabeça")
    print ("2 - inserir cauda")
    print ("3 - excluir cabeça")
    print ("4 - excluir cauda")
    print ("5 - mostrar pela cabeça")
    print ("6 - mostrar pela cauda")
    print ("7 - sair")
    opc = int(input("qual opção? "))
    return opc

def main():
    opc = 0
    lista = None
    deque = Deque()
    while opc != 7:
        opc = menu()
        if opc == 1:
            dado = int(input("dado para inserir: "))
            deque.cabecamais(dado)
        elif opc == 2:
            dado = int(input("dado para inserir: "))
            deque.caudamais(dado)
        elif opc == 3:
            deque.cabecamenos()
        elif opc == 4:
            deque.caudamenos()
        elif opc == 5:
            deque.mostrarcabeca()
        elif opc == 6:
            deque.mostrarcauda()

main()
