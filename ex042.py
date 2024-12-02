s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print('Com os segmentos informados é possível formar um triângulo do tipo:')
if s1 == s2 and s2 == s3:
    print('EQUILÁTERO')
elif s1 == s2 or s2 == s3 or s1 == s3:
    print('ISÓCELES')
else:
    print('ESCALENO')
