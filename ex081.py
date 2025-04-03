numeros = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N]: ')).upper().strip()
    if opção == 'N':
        break
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} números')
print(f'Os valores digitados em ordem foram {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
