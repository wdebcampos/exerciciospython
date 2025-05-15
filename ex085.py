num = list()
for i in range(1, 8):
    n = int(input(f"Digite o {i}º número: "))
    num.append(n)
num.sort()
print(f'Os valores pares digitados foram:', end=" ")
for i in num:
    if i % 2 != 0:
        print(i, end=" ")
print()
print(f'Os valores ímpares digitados foram:', end=" ")
for i in num:
    if i % 2 == 0:
        print(i, end=" ")
