print(f'{" Lojas Frederico ":=^40}')
preço = float(input('Preço do produto: R$ '))
condição_de_pagamento = int(input('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite uma opção: '''))
print('-=' * 20)
if condição_de_pagamento == 1:
    print(f'Você selecionou a opção à vista dinheiro/cheque')
    print(f'O valor do desconto é 10% (R$ {preço * 10 / 100:.2f})')
    print(f'O valor final é R$ {preço * 0.90:.2f}')
elif condição_de_pagamento == 2:
    print(f'Você selecionou a opção à vista cartão')
    print(f'O valor do desconto é de 5% (R$ {preço * 5 / 100:.2f})')
    print(f'O valor final é R$ {preço * 0.95:.2f}')
elif condição_de_pagamento == 3:
    print('Você selecionou a opção 2x no cartão')
    print(f'O valor de cada parcela é {preço / 2:.2f}')
    print(f'O valor final é R$ {preço}')
elif condição_de_pagamento == 4:
    print(f'Você selecionou a opção 3x ou mais vezes no cartão')
    parcela = int(input('Em quantas vezes quer parcelar: '))
    preço_parcela = float(preço / parcela)
    preço_parcela_juros = float(preço_parcela + (preço_parcela * 20 / 100))
    print(f'O valor de cada parcela é R$ {preço_parcela_juros:.2f}')
    print(f'O valor do produto é R$ {preço_parcela_juros * parcela:.2f}')
else:
    print('Opção inválida! Tente novamente.')
