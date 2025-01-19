num = (int(input('Digite um número ')),
       int(input('Digite um número ')),
       int(input('Digite um número ')),
       int(input('Digite um número ')))
print(f'Você digitou os valores:', ','.join(map(str, num)))
print(f'O número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 aparece na {num.count(3)}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitados foram: ', end='')
cont = 0
for n in num:
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
