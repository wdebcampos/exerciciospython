# Exercício Python 048: Faça um programa que calcule
# a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
total = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1 #pode ser cont += 1
        total = total + n # pode ser total += n
print(f'A soma de todos os {cont} valores é {total}')
