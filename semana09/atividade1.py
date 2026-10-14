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
        no = No(dado)
        if self.head == None:
            self.head = no
            self.tail = no
            return
        no.proximo = self.head
        self.head.anterior = no
        self.head = no
        return
    
    def rabomais(self, dado):
        no = No(dado)
        if self.head == None:
            self.head == self.tail == no
        no.anterior = self.tail
        self.tail.proximo = no
        self.tail = no
        return

    def removerfim(self):
        self.tail = self.tail.anterior
        self.tail.proximo = None
        return

    def removercomeco(self):
        self.head = self.head.proximo
        return

    def mostrar(self):
        aux = self.head
        while aux != None:
            print (aux.dado)
            aux = aux.proximo
        return


def menu():
    print("1 - add no fim da fila")
    print("2 - add no inicio da fila")
    print("3 - atender(remover) inicio da fila")
    print("4 - atender(remover) fim da fila")
    print("5 - mostrar tudo")
    print("6 - sair")
    opc = int(input("qual opção? "))
    return opc

def main():
    opc = 0
    deque = Deque()
    while opc != 6:
        opc = menu()
        if opc == 1:
            dado = int(input("qual o numero do chamado? "))
            deque.cabecamais(dado)
        elif opc == 2:
            dado = int(input("qual o numero do chamado? "))
            deque.rabomais(dado)
        elif opc == 3:
            deque.removerfim()
        elif opc == 4:
            deque.removercomeco()
        elif opc == 5:
            deque.mostrar()

main()
