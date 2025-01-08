print('=' * 40)
print(f'{' BANCO WBC ':^40}')
print('=' * 40)
nota50 = nota20 = nota10 = nota1 = 0
valor = int(input('Digite um valor para saque: R$ '))
total = valor
céd = 50
total_cedulas = 0
while True:
    if total >= céd:
        total -= céd
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        total_cedulas = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao Banco WBC')
