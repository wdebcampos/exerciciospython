num = []
num_pares = []
num_impares = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        num_pares.append(n)
    else:
        num_impares.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'A lista completa é {num}')
print(f'A lista de pares é {num_pares}')
print(f'A lista de impares é {num_impares}')
