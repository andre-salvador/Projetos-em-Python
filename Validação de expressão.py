from time import sleep
import os


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
    os.system('cls') or None
    expressao = str(input('Digite uma expressão: '))

    teste = checar(expressao)
    if teste:
        print('\nA expressão é valida!!')
        sleep(2)
    else:
        print('\nA expressão não é valida!!')
        sleep(2)
    
    escolha = ' '
    while escolha not in 'sn':
        os.system('cls') or None
        escolha = str(input('Deseja continuar[S/N]? ')).lower()
    
    if escolha == 'n':
        break

print('Obrigado por usar!!')
        