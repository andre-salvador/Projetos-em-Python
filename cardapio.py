import os

dic = {}
pedido_total = []
while True:
    dic.clear()
    os.system('cls') or None

    print('Escolha sua cerveja: ')
    print (' 1-ANTARTICA R$6.00;\n 2-SKOL R$6.50;\n 3-BRAHMA R$8.20;\n 4-SOL R$8.25;\n 5-NORTENHA R$16.80;\n 6-PROIBIDA R$4.80;')
    print(' 7-DEVASSA R$5.90;\n 8-HEINEKEN R$9.00')
           
    while True:
        beer = int(input("Número da Cerveja: "))

        if beer > 8:
            print('Digite um número entre 1 à 8')
        else:
            break

    quantidade = int(input('Quantas cervejas você deseja: '))

    if beer == 1:
        valor = float(6 * quantidade)
        nome = 'Antartica'
    
    elif beer == 2:
        valor = float(6.50 * quantidade)
        nome = 'Skol'
    
    elif beer == 3:
        valor = float(8.20 * quantidade)
        nome = 'Brahma'
    
    elif beer == 4:
        valor = float(8.25 * quantidade)
        nome = 'Sol'
    
    elif beer == 5:
        valor = float(16 * quantidade)
        nome = 'Nortenha'
    
    elif beer == 6:
        valor = float(4.80 * quantidade)
        nome = 'Proibida'
    
    elif beer == 7:
        valor = float(5.90 * quantidade)
        nome = 'Devassa'
    
    elif beer == 8:
        valor = float(9 * quantidade)
        nome = 'Heineken'
    
    dic['nome'] = nome
    dic['valor'] = valor
    dic['quantidade'] = quantidade
    pedido_total.append(dic.copy())

    while True:
        escolha = str(input('Deseja continuar[S/N]: ')).lower()[0]
        if escolha in 'sn':
            break
        print('ERRO!! Digite apenas S ou N')

    if escolha == 'n':
        break

os.system('cls') or None

total = 0
cervejas_compradas = []

for pedido in pedido_total:
    if pedido['nome']:
        cervejas_compradas.append(pedido['nome'])

    if pedido['valor']:
        total += pedido['valor']

print('-=' * 25)
print(f'Você comprou as cervejas: ', end='')
cont = 0
for p in cervejas_compradas:
    cont += 1
    print(f'{p}', end=', ') if cont != len(cervejas_compradas) else print(f'{p}', end='.')

print()
print(f'O valor total ficou: R${total}')