cont = soma = 0
while True:
    num = int(input('Digite um valor [999 para sair]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} e a soma é {soma}')
