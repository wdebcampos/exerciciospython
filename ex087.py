matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_3_coluna = maior_2_linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^7}]', end=' ')
        if matrix[l][c] % 2 == 0:
            pares += matrix[l][c]

    print()
print('=' * 40)

print(f'A soma dos valor pares é {pares} ')

for l in range(0, 3):
    soma_3_coluna += matrix[l][2]
print(f'A soma dos valores da terceira coluna é {soma_3_coluna} ')

for c in range(0, 3):
    if c == 1:
        maior_2_linha = matrix[1][c]
    elif matrix[1][c] > maior_2_linha:
        maior_2_linha = matrix[1][c]
print(f'O maior valor da segunda linha é {maior_2_linha} ')
