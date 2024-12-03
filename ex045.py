from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print(f'{"":=^20}')
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print(f'{"":=^20}')
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
