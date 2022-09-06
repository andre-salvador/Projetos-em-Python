from time import sleep


menu = 0 #variavel

#Looping 
while menu != 5:
    #menu inicial
    if menu == 0:
        print('-=-' * 21)
        print('Operações Matemáticas')
        print('-=-' * 21)

        #escolha dos números
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    
    #menu
    print('-=-' * 21)
    print(' 1- SOMAR \n 2- MULTIPLICAR \n 3- MAIOR \n 4- NOVOS NÚMEROS \n 5- SAIR')
    print('-=-' * 21)
    menu = int(input('Qual opção deseja: '))

    #operações
    if menu == 1:
        soma = n1 + n2
        print(f'A soma de {n1} com {n2} é igual a {soma}')
        sleep(1.5)

    elif menu == 2:
        multi = n1 * n2
        print(f'A multiplicação de {n1} com {n2} resulta em {multi}')
        sleep(1.5)

    elif menu == 3:
        if n1 > n2:
            print(f'O {n1} é maior que {n2}')
        else:
            print(f'O {n2} é maior que {n1}')
        sleep(1.5)
    
    elif menu == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        sleep(1.5)

    elif menu > 5:
        print('DIGITE UMA OPÇÃO VÁLIDA!!')
        sleep(1.5)