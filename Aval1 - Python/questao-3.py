#Arthur Oliveira, Italo Meireles, Vinicius Oliveira

listaBase = list()

#função para verificar se o número é par
def parItem(item):
    if item % 2 == 0:
        return True
    return False

#função para verificar se o número é impar
def imparItem(item):
    if item % 2 == 1:
        return True
    return False

#função que retorna se a sequência de números atende a questão
def m_alternativa(sequencia):
    k = 1
    i = 0
    fim = 0
    cont = 0
    lenSeg = 0
    #percorrendo a lista
    while(i < len(sequencia)):
        lenSeg = lenSeg + 1
        #pegando cada seguimento progressivamente (ex: [12] [3 7] [2 10 4] [5 13 5 11])
        seguimento = sequencia[i: i + k]
        item1 = seguimento[0]
        #verificando se o primeiro item do seguimento é par
        if parItem(item1):
            #verificando se cada item do seguimento é par, se for retorna cont = 1
            #se não, retorna como zero e para a repetição
            for item in seguimento:
                result = parItem(item)
                if result:
                    cont = 1
                else:
                    cont = 0
                    break
        #verificando se o primeiro item do seguimento é impar
        elif imparItem(item1):
            # verificando se cada item do seguimento é par, se for retorna cont = 1
            # se não, retorna como zero e para a repetição
            for item in seguimento:
                result = imparItem(item)
                if result:
                    cont = 1
                else:
                    cont = 0
                    break
        #somando o total de todas as listas que tinham par ou impar na sequencia correta
        fim = fim + cont
        i = i + k
        k = k + 1
    #verificando se o valor é igual ao valor da lista, se for, mostra o total na tela, se não
    #mostra que a lista não atende aos requisitos da questão
    if fim == lenSeg:
        print(fim)
        print('%')
    else:
        print('NAO')
        print('%')

seq = [
    [12, 3, 7, 2, 10, 4, 5, 13, 5, 11],
    [11, 2, 3, 4, 5, 77, 33, 44],
    [7, 30, 40, 13, 17, 99, 42, 76, 68, 88, 11, 22, 33, 44, 55, 90, 80, 70, 60, 50, 40, 51, 71, 81, 53, 97, 99],
    [10],
    [1, 2, 3]
]

#enviando cada item da lista para a função
for item in seq:
    m_alternativa(item)

