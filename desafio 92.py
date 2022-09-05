from datetime import date
import os


cadastro = {}

cadastro['nome'] = str(input('Nome: '))

#desafio: pegar idade da pessoa pelo seu ano de nascimento
ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
cadastro['idade'] = ano_atual - ano_de_nascimento

cadastro['ctps'] = int(input('Carteira de trabalho (0 caso não tiver): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['sálario'] = float(input('Salário: '))
    
    tempo_de_trabalho = ano_atual - cadastro['contratação']

    #foi considerado 35 anos de contribuição para ser aposentado
    if tempo_de_trabalho < 35:
        anos_restantes = 35 - tempo_de_trabalho
        cadastro['aposentadoria'] = cadastro['idade'] + anos_restantes
    
    #escolhi criar uma alternativa para quem ja pode aposentar/aposentado
    else:
        cadastro['aposentadoria'] = 'Aposentado'

    os.system('cls') or None  #comando para limpar o console
    #para acessar os itens de uma biblioteca é necessario colocar o .items()
    for item, valor in cadastro.items():
        print(f'{item}: {valor}')

else:
    os.system('cls') or None
    for item, valor in cadastro.items():
        print(f'{item}: {valor}')