#Vinicius Oliveira do Nascimento

#retorna uma lista de strings formatadas somente com numeros
def tranformarInt(novaLista):
    intLista = list()
    validacao = True
    #percorrenddo cada item da lista passada por parâmetros
    for item in novaLista:
        #percorrendo cada digito do item da lista passada por parâmetros
        for digito in item:
            #verificando se cada valor da lista é igual ou diferente de X, se for igual, modifica para 10, se
            #for uma lista que não seja de números, a lista é reiniciada e passa a instrução para terminar o for
            if digito == 'X':
                digito = '10'
            elif not digito.isnumeric():
                intLista = list()
                validacao = True
                break
            intLista.append(int(digito))
        if (validacao):
            break
    #retorno da nova lista com digitos
    return intLista

#função que executa a soma parcial sobre uma lista passada por parâmetros
def somaParcial(parcialLista):
    aux = 0
    semiLista = list()
    #retorna uma lista com a soma parcial da lista passada por parâmetros
    for item in range(len(parcialLista)):
        aux = parcialLista[item] + aux
        semiLista.append(aux)
    return semiLista

#retorna se as entradas do arquivo estão corretas ou não
def formatarIsbn(listaBase):
    novaLista = list()
    #substitui todos os caracteres '-' na lista passada por parâmetros
    for itemBase in listaBase:
        itemBase = itemBase.replace('-', '')
        novaLista.append(itemBase)

    intLista = tranformarInt(novaLista)
    #verifica se a lista transformada para inteiro é vazia
    #se não for, verifica se o 10º número é divisível por 11
    #se for, retorna que está correta, se não, retorna que está incorreto
    if len(intLista) == 0:
        print(''.join(listaBase), 'está incorreto.')
    else:
        semiLista = somaParcial(intLista)
        listaFinal = somaParcial(semiLista)
        if (listaFinal[len(listaFinal) - 1] % 11 == 0):
            print(''.join(listaBase), 'está correto.')
        else:
            print(''.join(listaBase), 'está incorreto.')

listaBase = list()
arquivo = open('p1_entrada1.txt','r')
#lendo os arquivos e adicionando o retorno para 'listaBase' sem quebras de linha
while 1:
    entrada = arquivo.readline().replace('\n','')
    #condição de parada de leitura do arquivo
    if entrada == '0-00000-000-0':
        break
    else:
        listaBase.append(entrada)

#passando cada item da lista para a função 'formatarIsbn' sem espaços
for i in listaBase:
    formatarIsbn(i.split())

