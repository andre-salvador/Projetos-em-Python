import random

#escolha de qual arquivo o player quer jogar
palavras =[]

while True:
    print(' [1] Animais\n [2] Profissões\n [3] Objetos')
    escolha_do_jogo = int(input('Quais palavras deseja jogar: '))

    if escolha_do_jogo == 1:
        with open('Palavras/animais.txt', 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                linha.strip().lower()
                palavras.append(linha)
        break
    
    elif escolha_do_jogo == 2:
        with open('Palavras/profissoes.txt', 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                linha.strip().lower()
                palavras.append(linha) 
        break
    
    elif escolha_do_jogo == 3:
        with open('Palavras/objetos.txt', 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                linha.strip().lower()
                palavras.append(linha) 
        break
    
    else:
        print('Escolha um número valido')

#escolha da palavra
num = random.randrange(0, len(palavras))
secreta = palavras[num]
print(secreta)
print(len(secreta))

palavra = []
for letra in secreta:
    palavra.append('_')
palavra.pop()
print(palavra)