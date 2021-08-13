def subtrair(num):
    return int(num) - int(num[::-1])


num = input('digite um numero ')
num = num.replace('-', '')
print(f'{num} - {num[::-1]} = {subtrair(num)}')