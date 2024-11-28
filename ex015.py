dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram percorridos: '))
qtdia = dias * 60
qtkm = km * 0.15
print(f'Pelo uso do carro alugado por {dias} dias e por ter percorrido {km}km, você pagará R${qtdia + qtkm :.2f}.')
