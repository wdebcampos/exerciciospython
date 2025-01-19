from  random import  randint

num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print(f'Os valors sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor foi o {max(num)}')
print(f'O menor valor foi o {(min(num))}')
