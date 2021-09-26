# Alunos: Dymas de Sousa Cunha e Vinicius Oliveira do Nascimento

class Game():
    def __init__(self, num_jogadores, tot_trilha, armadilhas):
        self.num_jogadores = num_jogadores
        self.tot_trilha = tot_trilha
        self.armadilhas = armadilhas

    def rodada(self, lances, lista_dados):
        jogador_atual = 0
        jogador_armadilha = None
        local_atual = 0

        for item in range(0, lances):
            
          if not (jogador_atual == jogador_armadilha):

            if jogador_atual >= self.num_jogadores:
                jogador_atual = 0

            local_atual = lista_dados[item] 

            if local_atual in self.armadilhas:
                jogador_armadilha = jogador_atual

            if local_atual >= self.tot_trilha:
                return (jogador_atual + 1)        
            jogador_atual = jogador_atual + 1

          jogador_atual = jogador_atual + 1
        return (jogador_atual + 1)
             
def main():
    lista_final = list()
    while True:
        entrada = list(map(int, input().split()))
        num_jogadores, num_trilha = entrada[0], entrada[1]
        if num_jogadores == 0 & num_trilha == 0:
            break
        armadilhas = list(map(int, input().split()))
        lance_dado = int(input())
        g1 = Game(num_jogadores, num_trilha, armadilhas)
        result = list()
        for i in range(0, lance_dado):
            dado = list(map(int, input().split()))
            result.append((dado[0] + dado[1]))
        final = g1.rodada(lance_dado, result)
        lista_final.append(final)

    for item in lista_final:
        print(item)

if __name__ == '__main__':
    main()