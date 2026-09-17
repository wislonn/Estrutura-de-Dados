class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura







def aaltura():
    altura = int(input("qual a altura do retangulo? "))
    return altura

def llargura():
    largura = int(input("qual a largura do retangulo? "))
    return largura


def menu():
    print ("")
    print ("1 - calcular área")
    print ("2 - calcular perimetro")
    print ("3 - sair")
    print ("")



def area(retangulo):
    print (retangulo.altura * retangulo.largura, "metros de área")
    return retangulo

def perimetro(retangulo):
    print (2*(retangulo.altura + retangulo.largura), "metros de perimetro")
    return retangulo



def main():
    altura = aaltura()
    largura = llargura()
    retangulo = Retangulo(altura, largura)
    opc = 0
    while opc != 3:
        menu()
        opc = int(input("qual o opção? "))
        if opc == 1:
            area(retangulo)
        elif opc == 2:
            perimetro(retangulo)
            


main()
