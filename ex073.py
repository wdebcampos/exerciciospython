import textwrap
times = ('Botafogo','Palmeiras', 'Flamengo', 'Fortaleza',
         'Internacional', 'São Paulo', 'Corinthians',
         'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG',
         'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
         'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('=' * 80)
print(f'{'5 PRIMEIROS COLOCADOS':^80}')
print(times[0:5])
print('=' * 80)
print('=' * 80)
print(f'{'4 ÚLTIMOS COLOCADOS':^80}')
print(times[-4:])
print('=' * 80)
print('=' * 80)
print(f'{'ORDEM DE ALFABÉTICA':^80}')
print(sorted(times))
print('=' * 80)
print('=' * 80)
print(f'{'POSIÇÃO DO TIME':^80}')
posição = str(input('Digite um time para ver a posição: ')).strip().title()
print(f'O {posição} está na {times.index(posição)+1}ª posição na tabela')
