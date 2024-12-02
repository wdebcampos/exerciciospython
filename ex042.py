s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print('ANALISADOR DE TRIÂNGULO')
if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    print('Com os segmentos informados é possível formar um triângulo do tipo: ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('ISÓCELES')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
else:
    print('Não é possível formar um triângulo')
