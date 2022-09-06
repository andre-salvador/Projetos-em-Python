n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
n3 = 10
total = 10

while n3 != 1:
    if n3 == 10:
        print(n1, end=(' ♠ '))
    n1 += n2
    print(n1, end=(' ♠ '))
    n3 -= 1
    if n3 == 1:
        print('\n')
        escolha = int(input('Quantos termos deseja saber mais? '))
        if escolha > 0:
            n3 += escolha
            total += escolha

print(f'Você viu um total de {total} termos')