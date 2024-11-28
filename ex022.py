nome = str(input('Digite seu nome completo: ')).strip() #esse strip é para retitar os espaços
print('analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
dividido = (nome.split())
print(f'Seu nome tem ao todo {len(''.join(dividido))} letras, sem os espaços.')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras.')
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
