print('CALCULADORA DE IMC')
peso = float(input('Digite o peso: (Kg) '))
altura = float(input('Digite a altura: (m) '))
imc = peso / (altura * altura)
print(f'O seu IMC é {imc:.2f}')
print(f'Sua classificação é: ', end= '')
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >=25 and imc < 30:
    print('Sobrepesso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')
