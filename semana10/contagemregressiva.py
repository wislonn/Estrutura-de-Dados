def contagem_regressiva(n):
    if n < 1:
        return
    print (n)
    contagem_regressiva(n - 1)


n = int(input("qual o numero? "))
contagem_regressiva(n)
