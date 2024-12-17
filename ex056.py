#Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for dados in range(1, 5):
    print(f'------- {dados}ª PESSOA -------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if dados == 1 and sexo in 'Mn':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
média_idade = soma_idade / 4
print(f'A média de idade do grupo é {média_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_velho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
