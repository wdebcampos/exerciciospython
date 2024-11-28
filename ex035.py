print('-=' * 20)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Podem formar um triângulo')
else:
    print('Não podem formar um triângulo')
