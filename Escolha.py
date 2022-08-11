from random import randint
#entrada do jogo
print('-' * 40)
print(f'{"JOGO DE ADVINHAÇÃO":^40}')
print('-' * 40)

#numros de tentativas até agora
tentativas = 0

#escolha do computador
comp = randint(1, 100)

#game
while True:
    try:
        n1 = int(input('Digite um número: '))
        
        if n1 == comp: #vitoria
            tentativas += 1
            break
        else:
            if tentativas >= 3 and n1 < comp: #dica para chutar mais alto
                print('Chuta mais ALTO...\n')
                tentativas += 1
            
            elif tentativas >= 3 and n1 > comp: #dica para chutar mais baixo
                print('Chuta mais BAIXO...\n')
                tentativas += 1
            
            else:
                print('Você errou... Tente novamente\n') #primeiras 3 tentativas
                tentativas += 1
    except:
        print('Digite um número válido!!\n') #verificação do input

#finalização
print(f'\n\nParabéns!! Você conseguiu acertar. o computador pensou no {comp} e você usou {tentativas} tentativas')