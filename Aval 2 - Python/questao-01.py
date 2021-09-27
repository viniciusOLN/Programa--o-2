class Chocolates():

    def __init__(self, mindt,  lilka):
        self.mindt = mindt
        self.lilka = lilka
    
    def distribuicao(self, quant, capacidade):
       pos = list()
       for i in range(0, (quant)):
           if (self.mindt - capacidade[i]) >= 0:
               self.mindt = self.mindt - capacidade[i]
               pos.append((i + 1))
           elif (self.lilka - capacidade[i]) >= 0:
               self.lilka = self.lilka-capacidade[i]
           else:
               return 'Impossible to distribute'
       pos.insert(0, int(len(pos)))
       return pos

    def __str__(self):
        return f'{self.capacidade} {self.quant} {self.lilka} {self.mindt}'

def main():
   result = list()

   while True:
       chocolates = list(map(int, input().split()))
       
       if chocolates[0] == 0 & chocolates[1] == 0:
           return False

       quant_caixas = int(input())
       capacidade_caixa = list(map(int, input().split()))

       c1 = Chocolates(chocolates[0], chocolates[1])
       result.append(c1.distribuicao(quant_caixas, capacidade_caixa))

if __name__ == '__main__':
    main()
