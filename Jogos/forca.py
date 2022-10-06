from random import randrange

#escolha de qual arquivo o player quer jogar
def escolha_palavras():
    palavras =[]

    while True:
        print(' [1] Animais\n [2] Profissões\n [3] Objetos')
        escolha_do_jogo = int(input('Quais palavras deseja jogar: '))

        if escolha_do_jogo == 1:
            with open('Palavras/animais.txt', 'r', encoding='UTF-8') as arquivo:
                for linha in arquivo:
                    linha.strip()
                    palavras.append(linha)
        
        elif escolha_do_jogo == 2:
            with open('Palavras/profissoes.txt', 'r', encoding='UTF-8') as arquivo:
                for linha in arquivo:
                    linha.strip()
                    palavras.append(linha)
        
        elif escolha_do_jogo == 3:
            with open('Palavras/objetos.txt', 'r', encoding='UTF-8') as arquivo:
                for linha in arquivo:
                    linha.strip()
                    palavras.append(linha)
        
        else:
            print('Escolha um número valido')
    
        return palavras

#escolhe e aleatoriza a palavra
def aleatorizador_palavras(palavras):
    num = randrange(0, len(palavras))
    palavra_escolhida = palavras[num].lower()
    return palavra_escolhida

#transforma a palavra em '_' para o print no jogo
def esconder_palavra(palavra_escolhida):
    return ['_' for i in palavra_escolhida]

#chute do jogador
def chute_jogador():
    try:
        chute = str(input('Digite uma letra: ')).strip().lower()
        return chute
    except:
        print('Digite uma letra válida!!')

#verificação do chute
def validacao_chute(chute, letra_correta, palavra_escolhida):
    index = 0
    for letra in palavra_escolhida:
        if chute == letra:
            letra_correta[index] = letra
        index += 1

#troféu
def mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("   ___________   ")
    print("  '._==_==_=_.'  ")
    print("  .-\:      /-.  ")
    print(" | (|:.     |) | ")
    print("  '-|:.     |-'  ")
    print("    \::.    /    ")
    print("     '::. .'     ")
    print("       ) (       ")
    print("     _.' '._     ")
    print("    '-------'    ")

#caveira
def mensagem_perdedor(palavra_escolhida):
    print('Puxa, você foi enforcado!')
    print(f'A palavra era {palavra_escolhida}')
    print('     _______________      ')
    print('    /               \     ')
    print('   /                 \    ')
    print(' //                   \/\ ')
    print(' \|   XXXX     XXXX   | / ')
    print('  |   XXXX     XXXX   |/  ')
    print('  |   XXX       XXX   |   ')
    print('  |                   |   ')
    print('  \__      XXX      __/   ')
    print('    |\     XXX     /|     ')
    print('    | |           | |     ')
    print('    | I I I I I I I |     ')
    print('    |  I I I I I I  |     ')
    print('    \_             _/     ')
    print('      \_         _/       ')
    print('        \_______/         ')

#desenho da forca
def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#estrutura do jogo
def jogo():
    print('*' * 33)
    print('***Bem vindo ao jogo da Forca!***')
    print('*' * 33)

    palavras = escolha_palavras()
    
    palavra_escolhida= aleatorizador_palavras(palavras)

    letra_correta = esconder_palavra(palavra_escolhida)
    letra_correta.pop()
    
    #variaveis
    acertou = False
    enforcou = False
    erros = 0
    letras_chutadas = []
    letras_faltando = len(letra_correta)

    #verificação
    print(letra_correta)
    while not enforcou and not acertou:
        
        chute = chute_jogador()

        #caso chute esteja certo
        if chute in palavra_escolhida:
            validacao_chute(chute, letra_correta, palavra_escolhida)
            letras_chutadas.append(chute)
            letras_faltando = str(letra_correta.count('_'))
            if letras_faltando == '0':
                print(f'PARABÉNS!! Você encontrou todas as letras formando a palavra {palavra_escolhida}')
        
        #caso a letra ja tenha sido chutada
        elif chute in letras_chutadas:
            print('Você ja chutou essa letra! tente outra')

        #caso chute errado
        else:
            erros += 1
            letras_chutadas.append(chute)
            print(letra_correta)
            print(f'Você errou!! ainda tem {7 - erros} tentativas')
            forca(erros)

        #verificação de vitoria ou derrota
        enforcou = erros == 7
        acertou = '_' not in letra_correta

        print(letra_correta)

    #mensagens finais
    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_escolhida)
    
    jogo()