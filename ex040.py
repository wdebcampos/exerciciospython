n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print(f'sua média é {média:.2f} e você está REPROVADO')
elif média >= 5 and média <= 6.9:
    print(f'Sua média é {média:.2f} e você está em RECUPERAÇÃO')
else:
    print(f'Sua média é {média:.2f} e você está APROVADO')
