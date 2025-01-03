total = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    total += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {total} e a somou {soma}')
