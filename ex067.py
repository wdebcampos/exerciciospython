print('-' * 35)
print(f'{'TABUADA':^35}')
print('-' * 35)
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('-' * 35)
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO')
