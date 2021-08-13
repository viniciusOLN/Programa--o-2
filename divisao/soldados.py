def contagemSoldados(n):
    cont = 0
    for k in range(1, n + 1):
        n = n - k
        cont = cont + 1
        if n == 0:
            return cont
            break
        elif n < 0:
            return cont
            break

def piramide(n):
    aux = 0
    for k in range(1, n + 1):
        aux = n
        n = n - k
        if n == 0:
            print(' X ' * k)
            break
        elif n < 0:
            print(' X ' * aux)
            break
        print(' X ' * k)

n = int(input('digite o numero de soldados '))
print(f'Total de filas: {contagemSoldados(n)}')
piramide(n)