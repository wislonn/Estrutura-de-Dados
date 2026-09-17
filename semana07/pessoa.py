class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


def apresentar_nome():
    nome = (input("qual seu nome? "))
    return nome


def apresentar_idade():
    idade = int(input("qual a sua idade? "))
    return idade


def apresentar_tudo(nome, idade):
    pessoa = Pessoa(nome, idade)
    print (pessoa.nome)
    print (pessoa.idade)



def main():
    idade = apresentar_idade()
    nome = apresentar_nome()

    apresentar_tudo(nome, idade)


main()
