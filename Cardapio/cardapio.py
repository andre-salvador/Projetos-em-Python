import os
import qrcode
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter


dic = {}
pedido_total = []

#Escolha da cerveja
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

    while True:  #verificação do pedido
        escolha = str(input('Deseja continuar[S/N]: ')).lower()[0]
        if escolha in 'sn':
            break
        print('ERRO!! Digite apenas S ou N')

    if escolha == 'n':
        break

os.system('cls') or None


#Tratativa dos itens
total_comprado = 0

for item in pedido_total:
    print(f'Você comprou {item["quantidade"]} {item["nome"]} e ficou R${item["valor"]:.2f}')
    print('=-' * 30)

    total_comprado += item['valor']

print(f'O valor total foi de R${total_comprado:.2f}')

print()
print(' 1- Cartão\n 2- Dinheiro\n 3- Pix\n 4- Boleto')

pagamento = int(input('Qual a forma de pagamento? '))

while True:
    if pagamento == 1:
        while True:    
                dividir = int(input('Quantas vezes deseja fazer: '))

                if dividir == 1:
                    print(f'O valor total ficou R${total_comprado}')
                    break

                elif dividir > 1:
                    print(f'Você escolheu dividir em {dividir} vezes, ficou no total de {total_comprado / dividir}')
                    break

                elif dividir == 0:
                    print('Digite um número igual ou maior que 1!!')

    elif pagamento == 2:
        print(f'Você ganhou um desconto de 5% o total ficou R${total_comprado - (total_comprado * 0.05)}')
        break

    elif pagamento == 3:
        pix_qrcode = qrcode.make('chave do pix')
        pix_qrcode.save('pix.png')
        pix = Image.open('pix.png')
        pix.show()
        break

    elif pagamento == 4:
        codigo = '0123456789012'

        codigo_barra = EAN13(codigo, writer=ImageWriter())
        codigo_barra.save("boleto")
        boleto = Image.open('boleto.png')
        boleto.show()
        break