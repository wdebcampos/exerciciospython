print('GERADOR DE PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 10
mais = 0
while total != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} -> ', end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais quer mostrar?  '))
print(f'Prossessão finalizada com {total} termos mostrados')
