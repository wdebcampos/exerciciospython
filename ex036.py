valor_da_casa = float(input('Qual o valor da casa: R$ '))
salário = float(input('Qual o valor do seu salário: R$ '))
prazo_pagamento = int(input('Em quanto anos você quer pagar: '))
prazo_pagamento = prazo_pagamento * 12
prestacao = valor_da_casa / prazo_pagamento
print('-='*10,'Banco do Brasil', '=-'*10)
if prestacao > (salário*0.3):
    print(f'Emprestimo NEGADO.')
    print(f'O valor da prestação é R$ {prestacao:.2f} e excede a 30% do seu salário (R$ {salário * 30 / 100:.2f}).')
else:
    print('Emprestimo Aprovado! ', end='')
    print(f'Com o salário de R$ {salário:.2f} você pode financiar \n um imóvel de R$ {valor_da_casa:.2f} com prazo de pagamento de {prazo_pagamento} meses \n sendo valor da prestação de R$ {prestacao:.2f}.')
print('-='*10,'Banco do Brasil', '=-'*10)
