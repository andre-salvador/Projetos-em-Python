n1 = int(input('Quantos elementos da fibonacci deseja saber? '))
ultimo = 0
penultimo = 1
print('0 ♠ 1', end=(' ♠ '))
cont = 2

while n1 > cont:
    termo = ultimo + penultimo
    ultimo = penultimo
    penultimo = termo
    print(termo , end=(' ♠ '))
    cont += 1