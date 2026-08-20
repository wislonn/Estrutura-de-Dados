class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None



def maiores (ist, n):
    while n is not None:
        if n.valor >= ist:
            print (n.valor, "é maior que", ist)
            n = n.proximo
        else:
            n = n.proximo



def main():
    n = No(10)
    n2 = No(5)
    n3 = No(50)

    n.proximo = n2
    n2.proximo = n3

    ist = int(input("qual o numero? "))
    ist = maiores (ist, n)

main()
