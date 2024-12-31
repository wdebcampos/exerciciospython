from time import sleep
from random import randint
computador = randint(0, 10)
print(f'{" JOGO DA ADIVINHAÇÃO ":=^42}')
print('Sou seu cumputador...')
print('Acabei de pesnar em um número entre 0 e 10')
print('Será se você consegue adivinhar qual foi?')
usuario = int(input('Qual é seu palpite?'))
print('Processando...')
sleep(1)
contador = 0
while usuario != computador:
    print('Palpite errado')
    print(f'O computador pensou {computador} e você digitou {usuario}')
    usuario = int(input('Digite o seu palpite novamente: '))
    contador += 1
print(f'Você acertou!')
print(f'O computador pensou {computador} e voc digitou {usuario}')
print(f'Foram necessário {contador} palpites até acertar!')
