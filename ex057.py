sexo = str(input('Digite o sexo: [M / F] ')).strip().capitalize()
while sexo not in 'MasculinomasculinoFemininofeminino':
    sexo = str(input('Dados inválidos. Digite o sexo novamente: ')).capitalize().strip()
print(f'Sexo {sexo} registrado com sucesso!')
