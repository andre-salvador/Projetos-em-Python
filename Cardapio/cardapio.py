import os
import qrcode
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter


pedido_total = []

#Colocando em dicionario ao inves de if e else
cardapio = [
    {'nome': 'Antartica', 'valor': 6.00},
    {'nome': 'Skol', 'valor': 6.50},
    {'nome': 'Brahma', 'valor': 8.20},
    {'nome': 'Sol', 'valor': 8.25},
    {'nome': 'Nortenha', 'valor': 16.00},
    {'nome': 'Proibida', 'valor': 4.80},
    {'nome': 'Devassa', 'valor': 5.90},
    {'nome': 'Heineken', 'valor': 9.00},
]

#Escolha da cerveja
while True:
    os.system('cls') or None

    #Print do menu
    print('Escolha sua cerveja: ')
    print('-=' * 17)
    for v, i in enumerate(cardapio):
        print(f'Cod: {v} {i["nome"]:.<15} R$ {i["valor"]:.2f}')

    print('-=' * 17)

    #verificação da escolha
    while True:
        beer = int(input("Código da Cerveja: "))

        if beer > 7:
            print('Digite um número entre 0 e 7')
        else:
            break

    quantidade = int(input('Quantas cervejas você deseja: '))  #Pegando informação da quantidade que o cliente deseja

    pedido = cardapio[beer].copy()
    pedido['quantidade'] = quantidade
    pedido['valor'] = pedido['valor'] * pedido['quantidade']  #pegando valor total

    pedido_total.append(pedido.copy())  #jogando tudo em um pedido final
    pedido.clear()

    #verificação do pedido
    while True:
        escolha = str(input('Deseja continuar[S/N]: ')).lower()[0]
        if escolha in 'sn':
            break
        print('ERRO!! Digite apenas S ou N')

    if escolha == 'n':
        break

os.system('cls') or None  #Limpesa da tela para que seja possivel ver os valores sem muita poluição


#Tratativa dos itens
total_comprado = 0

#mostrando os valores de forma separada
for item in pedido_total:
    print(f'Você comprou {item["quantidade"]} {item["nome"]} e ficou R${item["valor"]:.2f}')
    print('=-' * 30)

    total_comprado += item['valor']

#valor total da compra
print(f'O valor total foi de R${total_comprado:.2f}')

print()
#Métodos de pagamento
print(' 1- Cartão\n 2- Dinheiro\n 3- Pix\n 4- Boleto')

while True:
    pagamento = int(input('Qual a forma de pagamento? '))

    if pagamento <= 0 or pagamento > 4:
        print('Digite um número entre 1 e 4!!')

    #Cartão
    elif pagamento == 1:
        while True:    
            dividir = int(input('Quantas vezes deseja fazer: '))

            if dividir == 1:
                print(f'O valor total ficou R${total_comprado}')
                break

            elif dividir > 1:
                print(f'Você escolheu dividir em {dividir} vezes, ficou no total de R${total_comprado / dividir:.2f}')
                break

            else:
                print('Digite um número igual ou maior que 1!!')
        break

    #Dinheiro
    elif pagamento == 2:
        print(f'Você ganhou um desconto de 5% o total ficou R${total_comprado - (total_comprado * 0.05)}')
        break

    #Pix
    elif pagamento == 3:
        pix_qrcode = qrcode.make('chave do pix')
        pix_qrcode.save('pix.png')
        pix = Image.open('pix.png')
        pix.show()
        break
    
    #Boleto
    elif pagamento == 4:
        codigo = '0123456789012'

        codigo_barra = EAN13(codigo, writer=ImageWriter())
        codigo_barra.save("boleto")
        boleto = Image.open('boleto.png')
        boleto.show()
        break
