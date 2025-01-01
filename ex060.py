# from math import factorial
# num = int(input('Digite um número: '))
# fatorial = factorial(num)
# print(f'O fatorial do número {num}! é {fatorial}')

print('--- Mostrando o fatorial de um número ---')
num = int(input('Digite um número: '))
contador = num
f = 1
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f = f * contador
    contador = contador - 1
print(f)
