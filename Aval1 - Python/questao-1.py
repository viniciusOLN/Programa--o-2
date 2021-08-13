#Arthur Oliveira, Italo Meireles, Vinicius Oliveira

#retorna uma lista formatada somente com numeros inteiros
def formatarIsbn(listaBase):
    novaLista = list()
    for itemBase in listaBase:
        itemBase = itemBase.replace('-', '')
        novaLista.append(itemBase)
    novaLista = list(map(int, novaLista))
    return novaLista

#verifica se o ISBN repasssado é correto ou não
def verificarISbn(listaBase):
    novaLista = formatarIsbn(listaBase)
    print(novaLista)


listaBase = ['0-89237-010-6', '0-8306-3637-4', '0-8306-3637-5']

#listaBase = list()
#while 1:
    #a = input()
    #if a == '0-00000-000-0':
        #break
    #else:
        #listaBase.append(a)

verificarISbn(listaBase)

