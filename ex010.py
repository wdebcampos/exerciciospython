din = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 5.74
euro = 6.27
libra = 7.48
print(f'Com R${din:.2f} você pode comprar: \n US${din / dolar :.2f} \n €${din / euro :.2f} \n £${din / libra :.2f}')
