class peca:
    def __init__(self, ladoE, ladoD):
        self.ladoE = ladoE
        self.ladoD = ladoD

    def __str__(self):
        return f'{self.ladoE}|{self.ladoD}'

    def confirmaPeca(self):
        pass

def main():
    n = int(input(''))
    for i in range(0, n):
        domino = input('').split()
        novaPeca = peca(int(domino[0]), int(domino[1]))
        novaPeca.confirmaPeca()

if __name__ == '__main__':
    main()