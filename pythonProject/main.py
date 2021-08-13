def maior_valor(valor1, valor2):
    if (valor1 > valor2):
        print('O maior valor é: ', valor1)
    else:
        print('O maior valor é: ', valor2)


while (1):

    print('1. maior valor  2. Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
      x = int(input('Digite o primeiro valor '))
      y = int(input('Digite o segundo valor '))

      maior_valor(x, y)
      print('\n')
    elif op == 2:
        break
    else:
        print('Erro! tente novamente')

