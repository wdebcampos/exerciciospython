print('-' * 30)
print(f'{"SEQUÊNCIA DE FIBONACCI":^30}')
print('-' * 30)
n = int(input('Quantos termos quer mostrar: '))
t1 = 0
t2 = 1
cont = 3
if n == 1:
    print(t1, end='')
elif n == 2:
    print(t1, '->', t2, end='')
elif n >= 3:
    print(t1, '->', t2, end='')
    while cont <= n:
        t3 = t1 + t2
        print(f' -> {t3}', end='')
        cont += 1
        t1 = t2
        t2 = t3
print(' -> FIM')
