def num_perfect(num):
    sum = 0
    for d in range(1, num):
        if d % num == 0:
            sum = sum + num

    if sum < num:
        print(num, 'é um deficiente')
    elif sum > num:
        print(num, "é abundante")
    else:
        print(num,"é perfeito")



num = int(input("digite um numero"))

num_perfect(num)