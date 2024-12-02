n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirante {n1} e {n2} a média do aluno é {média}')
if média < 5:
    print(f'sua média é {média:.1f} e você está REPROVADO')
elif 6.9 >= média >= 5:
    print(f'Sua média é {média:.1f} e você está em RECUPERAÇÃO')
else:
    print(f'Sua média é {média:.1f} e você está APROVADO')
