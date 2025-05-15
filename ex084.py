pessoas = []
pesado = []
leve = []
mais_pesado = mais_leve = 0
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    person = [nome, peso]
    pessoas.append(person)
    if len(pessoas) == 1:
        mais_pesado = mais_leve = peso
        pesado.append(person)
        leve.append(person)
    else:
        if peso > mais_pesado:
            mais_pesado = peso
            pesado = [person]
        elif peso == mais_pesado:
            pesado.append(person)
        if peso < mais_leve:
            mais_leve = peso
            leve = [person]
        elif peso == mais_leve:
            leve.append(person)
    continue_input = input("Quer continuar? [S/N] ").strip().upper()
    if continue_input == 'N':
        break
print(f"\nForam cadastradas {len(pessoas)} pessoas.")
print(f"As pessoas mais pesadas ({mais_pesado}kg) são: {', '.join([p[0] for p in pesado])}.")
print(f"As pessoas mais leves ({mais_leve}kg) são: {', '.join([p[0] for p in leve])}.")