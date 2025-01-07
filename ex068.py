from random import randint
print('-=' * 20)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^40}')
print('-=' * 20)
vitoria_jogador = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    soma = jogador + computador
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Ímpar [P/I]? ')).upper().strip()
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} ', end='')
    print(' >>> PAR' if soma % 2 == 0 else ' >>> ÍMPAR')
    if opção == 'P':
        if jogador % 2 == 0:
            print('Você VENCEU')
            vitoria_jogador += 1
        else:
            print('Você PERDEU')
            break
    if opção == 'I':
        if jogador % 2 != 0:
            print('Você VENCEU')
            vitoria_jogador += 1
        else:
            print('Você PERDEU')
            break
print(f'!!! GAME OVER !!! Você venceu {vitoria_jogador} vezes')
