import os

dic = {}
total = []
while True:
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
    print('você escolheu a {}, {} unidades. Ficou R${} no total'.format(nome, quantidade, valor))
    total.append(dic.copy())

    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja pedir mais cerveja[S/N]: ')).lower().strip()
    
    if escolha == 'n':
        break

os.system('cls') or None
for i in total:
    print(i)