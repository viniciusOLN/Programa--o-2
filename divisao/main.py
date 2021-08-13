def divisao(num):
    w = len(str(num))
    div = 2
    while(num != 1):
        if num % div == 0:
            msg = '%*d|%d' % (w, num, div)
            print(msg)
            num = num // div
        else:
            div = div + 1
    msg = '%*d|' % (w, num)
    print(msg)

divisao(int(input('digite um numero ')))