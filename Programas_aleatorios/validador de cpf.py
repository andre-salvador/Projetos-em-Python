def validacao(cpf):
    cpf_final = cpf[:-2]
    cont = 10
    total = 0
    for index in range(19):
        if index > 8:
         index -= 9

        total += int(cpf_final[index]) * cont  

        cont -= 1
        if cont < 2:
            cont = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            cpf_final += str(d) 
    
    sequencia = cpf_final == str(cpf_final[0]) * len(cpf)

    if cpf == cpf_final and not sequencia:
        print('Válido')
    else:
        print('Inválido')


def gerador_de_cpf():
    from random import randint
    cpf_gerado = str(randint(1000000000, 9999999999))

    cont = 10
    total = 10
    for index in range(19):
        if index > 8:
            index -= 9
        
        total += int(cpf_gerado[index]) * cont
        cont -= 1

        if cont < 2:
            cont = 11
            d = 11 - (total % 11)
        
            if d > 9:
                d = 0
            total = 0
            cpf_gerado += str(d)
    
    print(cpf_gerado)


print('1 - Validar cpf \n2 - Gerar cpf')
escolha = int(input('Qual opção deseja: '))


if escolha == 2:
    gerador_de_cpf()



if escolha == 1:

    cpf = str(input('Informe o cpf: '))
    
    if len(cpf) > 11:
        novo_cpf = f'{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:14]}'
        validacao(novo_cpf)

    else:
        validacao(cpf)