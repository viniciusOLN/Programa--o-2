from random import randint

MAX_GUESSES = 5

def jogo(limit):
    numSorte = randint(1, 100)
    print("voce terá 5 chances para acertar o número selecionado aleatoriamente. boa sorte")
    for n in range(0, limit):
     print("palpite nº",n+1,":")
     num = int(input())
     if (num > numSorte):
         print("PALPITE ALTO DEMAIS")
     elif (num < numSorte):
         print("PALPITE BAIXO DEMAIS")
     else:
         print("PARABÉNS! VOCÊ ACERTOU O PALPITE!")
         break

    if(n == (limit-1)):
        print("fim dos palpites")


jogo(MAX_GUESSES)
