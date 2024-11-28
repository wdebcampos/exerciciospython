from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co **2 + ca **2) ** (1/2)
print(f'O valor da hipotenusa é {hi:.2f}')

# pode ser feito de outra forma usando o metódo

hi_math = hypot(co, ca)
print(f'O valor da hipotenusa é {hi_math :.2f}')
