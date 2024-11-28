vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print(f'Você excedeu a velocidade de 80Km/h. Você foi multado em R${(vel - 80) * 7:.2f}.')
else:
    print('Você dirigiu no limite de velocidade. Parabéns!')
