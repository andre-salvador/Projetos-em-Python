jogador = {}
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    #coleta dos gols
    gols = []
    total = 0
    for i in range(1, partidas + 1):
        gol = int(input(f'Quantos gols ele fez na {i} partida: '))
        total += gol
        gols.append(gol)

    jogador['gols'] = gols
    jogador ['total'] = total
    
    time.append(jogador.copy())

    while True:
        escolha = str(input('Deseja continuar[S/N]: ')).lower()[0]
        if escolha in 'sn':
            break
        print('ERRO!! Digite apenas S ou N')

    if escolha == 'n':
        break

#Mostrando os dados no console
print('-' * 40)
print('cod ', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ' , end='')
    for dados in v.values():
        print(f'{str(dados):<15}', end='')
    print()

print('-' * 40)

while True:
    busca = int(input('Qual jogador deseja saber os dados, digite o código dele (999 para parar): '))
    if busca == 999:
        break
    
    if busca > len(time):
        print('ERRO!! esse jogador não existe, digite um jogador válido!!')

    else:
        print('== LEVANTAMENTO DO JOGADOR ==')
        for i, gol in enumerate(time[busca]['gols']):
            print(f'  No jogo {i + 1} fez {gol} gols!')
        print('-' * 40)
