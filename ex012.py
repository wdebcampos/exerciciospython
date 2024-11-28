prod = float(input('Qual é o preço do produto? R$ '))
#novo preço pode ser (preço * 5/100)
print(f'O produto que custava R${prod: .2f}, na promoção om desconto de 5% vai custar R$ {prod * 0.95 :.2f}.')
