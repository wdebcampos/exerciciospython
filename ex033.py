'''Exercício Python 033: Faça um programa que
leia três números e mostre qual é o maior e qual
é o menor.'''

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
lista = [n1, n2, n3]
print(f'O menor valor digitado foi o {min(lista)}')
print(f'O maior valor digitado foi o {max(lista)}')
print(f'O maior valor é {max(n1, n2, n3)}')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print(menor)

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 < n1 and n3 > n2:
    maior = n3
print(maior)
