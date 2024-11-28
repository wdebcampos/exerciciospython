salário_atual = float(input('Qual o salário do funcionário? R$ '))
if salário_atual > 1250:
    print(f'Quem ganhava R${salário_atual} passa a ganhar R${salário_atual * 1.1:.2f}')
else:
    print(f'Quem ganhava {salário_atual} passa a ganhar R$ {salário_atual * 1.15:.2f}')
