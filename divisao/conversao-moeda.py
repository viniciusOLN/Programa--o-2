def convert(total):
    moedas = 0
    valor = 50
    while (1):
        while(total != 0):
            if (total - valor >= 0):
                total = total - valor
                moedas = moedas + 1
            else:
                if (valor == 50):
                    print(f'{moedas} ', end = "")
                    valor = 10
                elif (valor == 10):
                    print(f'{moedas} ', end = "")
                    valor = 5
                elif (valor == 5):
                    print(f'{moedas} ', end = "")
                    valor = 1
                moedas = 0
        if total == 0:
            print(f'{moedas} ')
            break


convert(int(input('digite o valor a ser convertido')))

