produtos = ('Caderno', 12.90,
            'Lápis', 1.50,
            'Caneta', 1.80,
            'Régua', 3.20,
            'Livro', 25.90,
            'Mochila', 125.60,
            'Estojo', 14.70)
print('_' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f' R${produtos[pos]:7.2f}')
print('_' * 40)
