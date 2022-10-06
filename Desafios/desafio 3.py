import os

pessoa = {}
galera = []
soma = media = 0

os.system('cls') or None

while True:
    print('-=' * 20)

    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!! Digite apenas M ou F')

    galera.append(pessoa.copy())

    while True:
        escolha = str(input('Deseja continuar[S/N]: ')).lower()[0]
        if escolha in 'sn':
            break
        print('ERRO!! Digite apenas S ou N')

    if escolha == 'n':
        break

print('-=' * 20)
print(f'Foram cadastradas {len(galera)} pessoas')

media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')

print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')

print()
print('As pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} com {p["idade"]} anos ', end='')