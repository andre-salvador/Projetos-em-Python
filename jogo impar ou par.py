from random import randint

print('Vamos jogar Par ou Impar')

vitorias = 0
while True:
    #variaveis importantes durante o game
    escolha = str(input('Você quer ser Par ou Impar? [P/I]')).upper().strip()
    n = int(input('Digite o valor:'))
    computador = randint(1, 10)
    resultado = (n + computador) % 2 #soma para ver se o numero final é imper ou par

    #vitoria em impar
    if escolha == 'I' and resultado == 1:
        print(f'Você venceu, o computador escolheu {computador}!!')
        vitorias += 1
    
    #vitoria em par
    elif escolha == 'P' and resultado == 0:
        print(f'Você venceu, o computador escolheu {computador}!!')
        vitorias += 1
    
    #derrota
    else:
        print(f'Você perdeu, o computador escolheu {computador} e a soma deu {n + computador}')
        break

pt = 'vez'
if vitorias == 0:
    pt = 'nenhuma vez'
elif vitorias > 1:
    pt = 'vezes'

print(f'Você perdeu o jogo, e ganhou {vitorias} {pt}')