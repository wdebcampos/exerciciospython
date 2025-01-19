extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',  'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezeseis',
           'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    nún = int(input('Digite um número entre 0 e 20: '))
    if nún < 0 or nún > 20:
        print(f'tente novamente.', end='')
    else:
        print(extenso[nún])
    continuar = str(input('Quer continuar: ')).upper().strip()
    if continuar == 'N':
            break
print('fim do programa')
