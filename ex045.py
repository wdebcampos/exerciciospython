import random

opções_usuario = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? 
'''))
print(f'{"JOKENPO":=^40}')
computador = int(random.randint(0, 2))
print('Computador jogou ', end='')
if computador == 0:
    print('PEDRA')
elif computador == 1:
    print('PAPEL')
elif computador == 2:
    print('TESOURA')
print('Jogador jogou ', end='')
if opções_usuario == 0:
    print('PEDRA')
elif opções_usuario == 1:
    print('PAPEL')
elif opções_usuario == 2:
    print('TESOURA')
print(f'{"JOKENPO":=^40}')
if computador == 0 and opções_usuario == 0:
    print(f'Jogo empate')
elif computador == 0 and opções_usuario == 1:
    print('Jogador venceu')
elif computador == 0 and opções_usuario == 2:
    print('Computador venceu')
elif computador == 1 and opções_usuario == 0:
    print('Computador venceu')
elif computador == 1 and opções_usuario == 1:
    print('Jogo empate')
elif computador == 1 and opções_usuario == 2:
    print('Jogador venceu')
elif computador == 2 and opções_usuario == 0:
    print('Jogador venceu')
elif computador == 2 and opções_usuario == 1:
    print('Computador venceu')
elif computador == 2 and opções_usuario == 2:
    print('Jogo empate')
