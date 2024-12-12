# Exercício Python 047: Crie um programa que mostre
# na tela todos os números pares que estão no intervalo
# entre 1 e 50

for pares in range(1, 51):
    if pares % 2 == 0:
        print(pares, end=' ')
print('Acabou')

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
# esa segunda opção utiliza menos memória e é mais rápido
