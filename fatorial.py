print('----- FATORIAL -----')

n1 = n2 = int(input('Informe o número que deseja fatorar: '))
resultado = n1
print(f'Calculando {n2}!', end=(' '))
while n1 != 1:
    n1 -= 1
    resultado *= n1
    print(n1, 'x ' if n1 != 1 else '= ', end=(''))

print(f'{resultado}')