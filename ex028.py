from random import randint
from time import sleep
pc = randint(0,5)
print('=-=' * 20)
print('Vou pensar em um número ente 0 e 5. Tente adivinhar...')
print('+-=' * 20)
vc = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(3)
if pc == vc:
    print(f'GANHEI! Eu pensei no número {pc} e não no {vc}!')
else:
    print(f'Você perdeu usuário. Eu pensei no {pc}')
