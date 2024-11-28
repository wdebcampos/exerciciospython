import math

angulo = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print(f'Em um ângulo de {angulo} o Seno é {s:.2f} o Cosseno é {c:.2f} e a Tangente é {t:.2f}.')
