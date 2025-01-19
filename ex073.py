import textwrap
times = ('Botafogo','Palmeiras', 'Flamengo', 'Fortaleza',
         'Internacional', 'São Paulo', 'Corinthians',
         'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG',
         'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
         'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('=' * 80)
print(f'{'5 PRIMEIROS COLOCADOS':^80}')
print(times[0:6])
print('=' * 80)
print('=' * 80)
print(f'{'4 ÚLTIMOS COLOCADOS':^80}')
print(times[16:])
print('=' * 80)
print('=' * 80)
print(f'{'ORDEM DE CLASSIFICAÇÃO':^80}')
print(sorted(times))
print('=' * 80)
print('=' * 80)
print(f'{'POSIÇÃO DO TIME':^80}')
posição = str(input('Digite um time para ver a posição: ')).strip().title()
print(f'O {posição} está na {times.index(posição)}ª posição na tabela')
