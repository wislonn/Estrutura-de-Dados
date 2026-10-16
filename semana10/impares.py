def contagempar(n):
    if n < 0:
        return
    if n % 2 == 1:
        print(n)
    contagempar(n - 1)

n = int(input("qual o numero? "))
contagempar(n)
