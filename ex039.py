ano_nascimento = int(input('Ano do nascimento: '))
ano_atual = 2024
if ano_atual - ano_nascimento > 18:
    print('Já passou do tempo de você se alistar')
    print(f'Você deveria ter se alistado em {ano_nascimento + 18}')
elif ano_atual - ano_nascimento == 18:
    print('Você deve se alistar IMEDIATAMENTE')
else:
    print('Você ainda vai se alistar')
    print(f'Falta {ano_atual - ano_nascimento} anos para você se alistar')
