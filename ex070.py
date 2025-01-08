print('-' * 30)
print(f'{'LOJA WBCAMPOS':^30}')
print('-' * 30)
total_gasto = 0
prod_mais_1000 = 0
nome_prod_mais_barato = ''
preço_mais_barato = 0
cont = 0
while True:
    nome_produto = str(input('Produto: '))
    preço_produto = float(input('Preço: R$ '))
    total_gasto += preço_produto
    cont += 1
    if preço_produto > 1000:
        prod_mais_1000 += 1
    if cont == 1 or preço_produto < preço_mais_barato:
        preço_mais_barato = preço_produto
        nome_prod_mais_barato = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        print(f'{' FIM DA COMPRA ':-^30}')
        break
print(f'Total da compra: R$ {total_gasto:.2f}')
print(f'{prod_mais_1000} produtos custaram mais que R$ 1.000,00')
print(f'O produto mais barato foi a(o) {nome_prod_mais_barato} que custa R${preço_mais_barato:.2f}')
