nome = str(input('Digite seu nome completo: ')).strip().split()
print(f'Muito prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {nome.split()[0]}.')
print(f'Seu último nome é {nome.split()[-1]}.')
