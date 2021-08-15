#Arthur Oliveira, Italo Meireles, Vinicius Oliveira

listaBase = list()
arquivo = open('p2_entrada2.txt','r')

# Pessoa Presente Passado Futuro
presente = ['o', 'os', 'a', 'om', 'ons', 'am']
passado =  ['ei', 'es', 'e', 'em', 'est', 'im']
futuro =   ['ai', 'ais', 'i', 'aem', 'aist', 'aim']
pessoa =   ['1', '2', '3', '4', '5', '6']

def formataSufixo(listaBase):
    #percorrendo cada item da lista passada por parâmetro
    for item in listaBase:
        pessoa_v = 0
        tempo = ''
        cort4 = item[len(item) - 4] + item[len(item) - 3] + item[len(item) - 2] + item[len(item) - 1]
        cort3 = item[len(item) - 3] + item[len(item) - 2] + item[len(item) - 1]
        cort2 = item[len(item) - 2] + item[len(item) - 1]
        cort1 = item[len(item) - 1]
        #verificando se a terminação do item está em algum dos tempos
        if cort4 in presente or cort4 in passado or cort4 in futuro:
            #verificando se o tamanho do item é maior que a terminação do item
            if len(item) > len(cort4):
                #verificando o tempo verbal
                if cort4 in presente:
                    pessoa_v = presente.index(cort4)
                    tempo = 'presente'
                elif cort4 in passado:
                    tempo = 'pretérito'
                    pessoa_v = passado.index(cort4)
                elif cort4 in futuro:
                    tempo = 'futuro'
                    pessoa_v = futuro.index(cort4)
                print(f'{item} - {item[0:len(item) - int(len(cort3) + 1)]}en, {tempo} {pessoa_v + 1}a pessoa')
            #caso o item seja menor q sua terminação
            else:
                print(f'{item} - não é tempo verbal')
        #verificando a terminação com 3 letras
        elif cort3 in presente or cort3 in passado or cort3 in futuro:
            #verificando se o tamanho do item é maior que a sua terminação
            if len(item) > len(cort3):
                #verificando o tempo verbal
                if cort3 in presente:
                    tempo = 'presente'
                    pessoa_v = presente.index(cort3)
                elif cort3 in passado:
                    tempo = 'pretérito'
                    pessoa_v = passado.index(cort3)
                elif cort3 in futuro:
                    tempo = 'futuro'
                    pessoa_v = futuro.index(cort3)
                print(f'{item} - verbo {item[0:len(item) - int(len(cort3))]}en, {tempo}, {pessoa_v + 1}a pessoa')
            #caso o item seja menor que sua terminação
            else:
                print(f'{item} - não é tempo verbal')
        #verificando a terminação com 2 letras
        elif cort2 in presente or cort2 in passado or cort2 in futuro:
            #verificando o tempo
            if cort2 in presente:
                tempo = 'presente'
                pessoa_v = presente.index(cort2)
            elif cort2 in passado:
                tempo = 'pretérito'
                pessoa_v = passado.index(cort2)
            elif cort2 in futuro:
                tempo = 'futuro'
                pessoa_v = futuro.index(cort2)
            print(f'{item} - verbo {item[0:len(item) - int(len(cort2))]}en, {tempo}, {pessoa_v + 1}a pessoa')
        #verificando a terminação com 1 letra
        elif cort1 in presente or cort1 in passado or cort1 in futuro:
            #verificando se termina com a
            if item[len(item) - 1] == 'a':
                #verificando se a penultima letra é diferente de vogal
                if item[len(item) - 2] == 'a' or item[len(item) - 2] == 'e' or item[len(item) - 2] == 'i' or item[len(item) - 2] == 'o' or item[len(item) - 2] == 'u':
                    print(f'{item} - não é tempo verbal')
                else:
                    #verificando o tempo
                    if cort1 in presente:
                        tempo = 'presente'
                        pessoa_v = presente.index(cort1)
                    elif cort1 in passado:
                        tempo = 'pretérito'
                        pessoa_v = passado.index(cort1)
                    elif cort1 in futuro:
                        tempo = 'futuro'
                        pessoa_v = futuro.index(cort1)
                    print(f'{item} - verbo {item[0:len(item) - int(len(cort2))]}en, {tempo}, {pessoa_v + 1}a pessoa')
            #caso seja diferente e a
            else:
                #verificando tempo verbal
                if cort1 in presente:
                    tempo = 'presente'
                    pessoa_v = presente.index(cort1)
                elif cort1 in passado:
                    tempo = 'pretérito'
                    pessoa_v = passado.index(cort1)
                elif cort1 in futuro:
                    tempo = 'futuro'
                    pessoa_v = futuro.index(cort1)
                print(f'{item} - verbo {item[0:len(item) - 1]}en, {tempo}, {pessoa_v + 1}a pessoa')
        #caso não atenda nenhuma das condições anteriores
        else:
            print(f'{item} - não é tempo verbal')

#lendo cada palavra do arquivo e retornando para uma lista sem quebra de linha
for palavra in arquivo.readlines():
    listaBase.append(palavra.replace('\n', ''))

formataSufixo(listaBase)
