class No:
    def __init__(self, carros):
        self.carros = carros
        self.proximo = None



def retirar(carros):
    print("aaaa")



def main():
    carros = None
    while carros != 20:
        carros += 1
        carros.proximo = carros
        print (carros.proximo)

main()
