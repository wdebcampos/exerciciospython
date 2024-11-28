distância = int(input('Digite a distância da viagem: '))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'Para um viagem de {distância} o valor da passagem é R${preço:.2f}')
