expressão = str(input('Digite a expressão para validar: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('expressão válida')
else:
    print('Expressão inválida')
