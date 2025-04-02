listnum = []
while True:
    num = int(input('Digite um valor: '))
    if num not in listnum:
        listnum.append(num)
        print('Valor adicionado na lista')
    else:
        print('Valor duplicado. Não adicionado na lista')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N]: ')).upper().strip()
    if opção == 'N':
        break
listnum.sort()

print(listnum)
