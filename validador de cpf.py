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


cpf = str(input('Digite seu CPF: '))

if len(cpf) > 11:
    novo_cpf = f'{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:14]}'
    validacao(novo_cpf)

else:
    validacao(cpf)