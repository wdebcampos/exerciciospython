média = soma = maior = menor = cont = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    continuar = str(input('Quer continuar [S ou N]: ')).strip()
print(f'Você digitou {cont} e a média dos valores digitados foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
