h = int(input("digite a altura do x: "))
aux = h

for i in range(1, h + 1):
    print(" "* i, end=" ")
    print('X', end=" ")
    print(" "*aux, end=" ")
    print('X')
    aux = aux - 1