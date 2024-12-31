from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opções = 0
while opções != 5:
    opções = int(input('''
    ---------------------------
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>> Digite a sua opção: '''))
    if opções == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é {soma}')
    elif opções == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {multiplicar}')
    elif opções == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número é o {maior}')
    elif opções == 4:
        n1 = int(input('Digite novo primeiro valor: '))
        n2 = int(input('Digite novo segundo valor: '))
    elif opções == 5:
        print('Fechando o programa', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
    else:
        print('Opção inválida!')
print('Fim!')
