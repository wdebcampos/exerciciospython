from datetime import date
sexo = str(input('''
Digite o sexo:
 [MAS] - Masculino
 [FEM] - Feminino
 ''')).upper()
if sexo == 'FEM':
    print('Você não precisa de alistar')
else:
    print('Você deve se alistar')
    ano_nascimento = int(input('Ano do nascimento: '))
    ano_atual = date.today().year
    print(f'Você nasceu em {ano_nascimento} e possui {ano_atual - ano_nascimento} anos em {ano_atual}')
    if ano_atual - ano_nascimento > 18:
        print('Já passou do tempo de você se alistar')
        print(f'Você deveria ter se alistado em {ano_nascimento + 18}')
    elif ano_atual - ano_nascimento == 18:
        print('Você deve se alistar IMEDIATAMENTE')
    else:
        print('Você ainda vai se alistar')
        print(f'Falta {18 - (ano_atual - ano_nascimento)} anos para você se alistar')
