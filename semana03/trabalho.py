class No:
    def __init__(self, nome, nota, id):
        self.nome = nome
        self.nota = nota
        self.id = id
        self.proximo = None
        self.anterior = None

def menu ():
    print("")
    print ("1 - inserir aluno")
    print ("2 - listar alunos")
    print ("3 - remover aluno")
    print ("4 - buscar aluno")
    print ("5 - mostrar situação dos alunos")
    print ("6 - sair")
    print("")
    return





def inserir (lista, nome, id, nota):
    novo = No(nome, nota, id)

    if lista == None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista
    



def mostrar (lista, nome, id , nota):
    aux = lista

    while aux != None:
        print (aux.nome, " #", aux.id)
        #print ("nota: ", aux.nota)
        aux = aux.proximo
    return lista

def remover (lista, nome, id, nota):
    aux = lista

    if lista == None:
        print ("lista vazia")
        return

    
    while aux != None:
        if aux.nome == nome:
            if aux.proximo == aux.anterior == None:
                lista = (None)
                return lista
            elif aux.proximo == None:
                lista = aux.anterior.proximo = None
                return lista



def main():
    nome = None
    id = 0
    nota = None
    opc = 0
    lista = None
    while opc != 6:
        menu()
        opc = int(input("qual a opção? "))
        if opc == 1:
            nome = (input("qual o nome dele? "))
            #id = int(input("qual o ID dele? "))
            #nota = float(input("qual a nota dele? "))
            lista = inserir(lista, nome, id, nota)
        elif opc == 2:
            lista = mostrar (lista, nome, id, nota)
        elif opc == 3:
            nome = (input("qual aluno você quer remover? "))
            lista = remover (lista, nome, id, nota)



main()
