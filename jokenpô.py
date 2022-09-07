from random import choice

#Apresentação do jogo
print('-=-' *20)
print('Bem-Vindo ao jogo Jokenpô')
print('-=-' *20)

#Escolha do computador
itens = ['Pedra', 'Papel', 'Tesoura']
computador = choice(itens)

#Escolha do jogador
print(' 1- Pedra \n 2- Papel \n 3- Tesoura')
while True:
    escolha = int(input('Escolha sua jogada: '))

    #Conversão da escolha do jogador
    if escolha == 1:
        escolha = 'Pedra'
        break
    
    elif escolha == 2:
        escolha = 'Papel'
        break
    
    elif escolha == 3:
        escolha = 'Tesoura'
        break
    
    else:
        print('ERRO! Escolha um número entre 1 e 3!!!')

#empate
if computador == 'Pedra' and escolha == 'Pedra':
    print('Deu empate, ambos escolheram Pedra')

elif computador == 'Papel' and escolha == 'Papel':
    print('Deu empate, ambos escolheram Papel')

elif computador == 'Tesoura' and escolha == 'Tesoura':
    print('Deu empate, ambos escolheram Tesoura')

#Vitória do Computador
if computador == 'Pedra' and escolha == 'Tesoura':
    print('O computador ganhou!! ele escolheu Pedra')

elif computador == 'Papel' and escolha == 'Pedra':
    print('O computador ganhou!! ele escolheu Papel')

elif computador == 'Tespura' and escolha == 'Papel':
    print('O computador ganhou!! ele escolheu Tesoura')

#Vitoria do jogador
if escolha == 'Pedra' and computador == 'Tesoura':
    print('Você venceu!! O computador escolheu Tesoura')

if escolha == 'Papel' and computador == 'Pedra':
    print('Você venceu!! O computador escolheu Pedra')

if escolha == 'Tesoura' and computador == 'Papel':
    print('Você venceu!! O computador escolheu Papel')