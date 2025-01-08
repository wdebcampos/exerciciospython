print('-' * 30)
print(f'{'CADASTRE UMA PESSOA':^30}')
print('-' * 30)
pessoas_mais_18_anos = homens_cadastrados = mulheres_menos_20_anos = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        pessoas_mais_18_anos += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulheres_menos_20_anos += 1
    if sexo == 'M':
        homens_cadastrados += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('-' * 30)
print('-' * 35)
print(f'{pessoas_mais_18_anos} pessoas tem mais de 18 anos')
print(f'Foram cadastrados {homens_cadastrados} homens')
print(f'{mulheres_menos_20_anos} mulheres tem menos de 20 anos')
