lista_num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista_num.append(n)
        print('Adicionado ao final da lista...')
    elif n > lista_num[-1]:
        lista_num.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista_num):
            if n <= lista_num[pos]:
                lista_num.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista_num}')
