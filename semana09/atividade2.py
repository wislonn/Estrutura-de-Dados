class No():
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None
        self.anterior = None
class Deque():
    def __init__(self):
        self.head = None
        self.tail = None



    def addhead(self, pessoa):
        no = No(pessoa)
        if self.head == None:
            self.head = self.tail = no
            return

        no.proximo = self.head
        self.head.anterior = no
        self.head = no
        return

    def addtail(self, pessoa):
        no = No(pessoa)
        if self.head == None:
            self.head = self.tail = no
            return

        no.anterior = self.tail
        self.tail.proximo = no
        self.tail = no
        return

    def remover(self):
        self.tail = self.tail.anterior
        self.tail.proximo = None
        return

    def mostrar(self):
        aux = self.head
        while aux != None:
            print(aux.pessoa)
            aux = aux.proximo
        return


def menu():
    print("1 - add cliente comumm")
    print("2 - add cliente preferencial")
    print("3 - atender")
    print("4 - mostrar")
    print("5- sair")
    opc = int(input("qual opção? "))
    return opc

def main():
    opc = 0
    deque = Deque()
    while opc != 5:
        opc = menu()
        if opc == 1:
            pessoa = input("qual o nome do sujeito? ")
            deque.addhead(pessoa)
        elif opc == 2:
            pessoa = input("qual o nome do sujeito preferencial? ")
            deque.addtail(pessoa)
        elif opc == 3:
            deque.remover()
        elif opc == 4:
            deque.mostrar()
main()
