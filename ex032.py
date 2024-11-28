from datetime import date
ano = int(input('Digite o ano que quer analisar? Coloque 0 para ano atual: '))
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or 2024 % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é bissexto.')
