def checar(exp):
    testa = []
    for i in exp:
        if i == '[' or i == '(' or i == '{':
            testa.append(i)
        
        if i == ']':
            if testa[-1] == '[':
                testa.pop()
            else:
                return False
        
        elif i == '}':
            if testa[-1] == '{':
                testa.pop()
            else:
                return False
        
        elif i == ')':
            if testa[-1] == '(':
                testa.pop()
            else:
                return False
        
    return True if len(testa) == 0 else False


while True:
    expressao = str(input('Digite uma expressão: '))

    teste = checar(expressao)
    if teste:
        print('A expressão é valida!!')
    else:
        print('A expressão não é valida!!')
    
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja continuar[S/N]? ')).lower()
    
    if escolha == 'n':
        break

print('Obrigado por usar!!')
        