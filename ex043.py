print('CALCULADORA DE IMC')
peso = float(input('Digite o peso: (Kg) '))
altura = float(input('Digite a altura: (m) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
print(f'Sua classificação é: ', end= '')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 >= imc < 25:
    print('Peso ideal')
elif 25 >= imc < 30:
    print('Sobrepesso')
elif 30 >= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade morbida')
